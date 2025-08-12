from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException, Request, Depends, Cookie, Response
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional, List
import logging
import os
import jwt
import pytz
from time import time
from secrets import token_urlsafe
import hashlib

from backend.src.utils.logging_config import configure_logging
from backend.src.utils import user_creation
from backend.src.utils.workout.workout_database import workout_database
from backend.src.main.API.initial_user_to_sql import main as SurveyMain
from backend.config import DB_CREDENTIALS, SECRET_KEY
from backend.src.utils.SQLutils.user_retrieve import populate_user_info
from backend.src.utils.user_storage.user import user
from backend.src.utils.pace_calculations import to_str
from backend.src.utils.SQLutils.user_send import send_user_creds

log_level_str = os.getenv("LOG_LEVEL", "DEBUG").upper()
log_level = getattr(logging, log_level_str, logging.DEBUG)
configure_logging(level=log_level)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable not set")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 30


def _hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


REFRESH_TOKENS: dict[str, dict] = {}
USER_REFRESH_TOKENS: dict[int, str] = {}

def create_access_token(user_id: int, expires_delta: timedelta | None = None) -> str:
    to_encode = {"user_id": user_id}
    expire = datetime.now(pytz.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    logger.debug(
        "Created access token for user_id=%s exp=%s", user_id, expire.isoformat()
    )
    return token


def create_refresh_token(user_id: int) -> str:
    token = token_urlsafe(32)
    expire = datetime.now(pytz.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    hashed = _hash_token(token)
    old = USER_REFRESH_TOKENS.get(user_id)
    if old:
        REFRESH_TOKENS.pop(old, None)
    REFRESH_TOKENS[hashed] = {"user_id": user_id, "expires": expire}
    USER_REFRESH_TOKENS[user_id] = hashed
    logger.debug(
        "Issued refresh token for user_id=%s exp=%s hash=%s",
        user_id,
        expire.isoformat(),
        hashed[:8],
    )
    return token


def rotate_refresh_token(token: str) -> tuple[int, str]:
    hashed = _hash_token(token)
    data = REFRESH_TOKENS.get(hashed)
    if not data or data["expires"] < datetime.now(pytz.utc):
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    user_id = data["user_id"]
    REFRESH_TOKENS.pop(hashed, None)
    USER_REFRESH_TOKENS.pop(user_id, None)
    new_token = create_refresh_token(user_id)
    logger.debug(
        "Rotated refresh token for user_id=%s old_hash=%s", user_id, hashed[:8]
    )
    return user_id, new_token


def verify_token(token: str) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        logger.debug("Verified access token for user_id=%s", user_id)
        return int(user_id)
    except jwt.PyJWTError as e:
        logger.warning(
            "JWT verification failed: %s: %s",
            e.__class__.__name__,
            str(e),
        )
        raise HTTPException(status_code=401, detail="Invalid token")


async def get_current_user(token: str | None = Cookie(None)) -> int:
    
    if not token:
        logger.debug("Authentication token missing from cookies")
        raise HTTPException(status_code=401, detail="Missing authentication token")
    # logger.debug("Authentication token received: %s", token[:8] + "...")
    return verify_token(token)


# Simple in-memory login attempt tracker to mitigate brute-force attacks.
LOGIN_ATTEMPTS = {}
MAX_ATTEMPTS = 5
BLOCK_TIME = 300  # seconds


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log request and response details.

    Debug-level logging provides insight during test runs without cluttering
    production logs when the log level exceeds ``DEBUG``.
    """
    start_time = time()
    if logger.isEnabledFor(logging.DEBUG):
        headers = {
            k: v for k, v in request.headers.items()
            if k.lower() != "authorization"
        }
        query = {
            k: ("***" if "token" in k.lower() or "key" in k.lower() else v)
            for k, v in request.query_params.items()
        }
        
        cookies = {
            k: (v[:8] + "..." if "token" in k.lower() else v)
            for k, v in request.cookies.items()
        }
        logger.debug(
            "%s %s from %s query=%s headers=%s  cookies=%s",
            request.method,
            str(request.url),
            request.client.host,
            query,
            headers,
            cookies,
        )
    else:
        logger.debug("%s %s from %s", request.method, request.url.path, request.client.host)

    response = await call_next(request)
    duration = (time() - start_time) * 1000
    logger.debug(
        "Completed %s %s with %d in %.2fms",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )
    return response


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """Log unhandled exceptions with stack traces."""
    logger.exception("Unhandled exception for %s %s", request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


@app.get("/")
async def root(request: Request):
    """Simple health-check endpoint for the API root."""
    logger.info("Health check from %s", request.client.host)
    return {"message": "AI Training Plans API is running"}


class SurveyIn(BaseModel):
    """SurveyIn is a Pydantic model that represents the input for the preliminary survey.
    """
    date_of_birth: str
    sex: str
    running_experience: str
    major_injuries: int
    most_recent_injury: int
    longest_run: int
    goal_date: str
    days_per_week: int
    days_of_week: list
    most_time_day: str
    current_5k_fitness: int

# Endpoint for preliminary survey


class Post_Run_SurveyIn(BaseModel):
    """Post_Run_SurveyIn is a Pydantic model that represents the input for the post run survey.
    """
    workout_rpe: dict
    completion: bool
    mileage: int
    reps: int
    pace: int


class HomeData(BaseModel):
    """HomeData is a Pydantic model that represents the data returned for the home page.
    """
    day: str  # A day of form "Friday, July 25"
    mileage: float  # e.g. 3.5
    pace: str  # e.g. "7:00-7:30"
    stimuli: str  # looks liek "Progression Run + Strides", or something of that form
    goal_rpe: str  # e.g. "5/10"
    time: str  # e.g. "0:57-0:59" // today's workout time, if applicable
    upcoming: str  # e.g. "Easy Run" // next days workout type
    upcomingmileage: float  # e.g. 3.5 // next days workout mileage, if applicable
    upcomingtime: str  # e.g. "0:57-0:59" // next days workout time, if applicable
    weeknum: List[int]  # e.g. 1 // the week number of the current week
    # e.g. 30.5 // the total mileage of the current week
    weekmileage: List[float]
    # e.g. 0.5 // the percentage of the current week that is complete
    weekpctcomplete: List[float]
    weekstimuli: List[str]  # Such as "Build" or "Maintain"


class SignupIn(BaseModel):
    """SignupIn is a Pydantic model that represents the input for user signup.
    """
    email: str
    username: str
    password: str


class LoginIn(BaseModel):
    """LoginIn is a Pydantic model that represents the input for user login.
    """
    username: str
    password: str


class AuthOut(BaseModel):
    """AuthOut is a Pydantic model that represents the output for user authentication (login and signup)
    """
    user_id: Optional[int] = None
    error_code: Optional[int] = None


@app.post("/survey/prelim")
async def survey_prelim(payload: SurveyIn, current_user: int = Depends(get_current_user)):
    """survey_prelim is an endpoint that handles the preliminary survey for a user.

    Args:
        payload (SurveyIn): A Pydantic model that contains the user's responses to the preliminary survey.

    Raises:
        HTTPException: If an error occurs during the processing of the survey, an HTTPException is raised with a status code of 500 and the error message.

    Returns:
        str: A string containing the status of the survey submission, typically an acknowledgment of successful processing.
    """
    try:
        data = payload.model_dump()
        data["user_id"] = current_user
        result = SurveyMain.prelim_survey(data)

        return result
    except Exception as e:
        # surface errors as HTTP 500 and log to the log file
        logger.exception(
            "Unexpected error in /survey/prelim for user_id=%s", current_user)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/post_run_survey")
async def post_run_survey(payload: Post_Run_SurveyIn, current_user: int = Depends(get_current_user)):
    """post_run_survey is an endpoint that handles the post run survey of a user

    Args:
        payload (Post_Run_SurveyIn): A Pydantic model that contains the user's responses to the preliminary survey.

    Raises:
        HTTPException: If an error occurs during the processing of the survey, an HTTPException is raised with a status code of 500 and the error message.

    Returns:
        str: A string containing the status of the survey submission, typically an acknowledgment of successful processing.
    """
    try:
        data = payload.model_dump()
        data["user_id"] = current_user
        result = SurveyMain.post_run_survey(data)

        return result
    except Exception as e:
        # surface errors as HTTP 500

        raise HTTPException(status_code=500, detail=str(e))


@app.get("/home/data", response_model=HomeData)
async def get_home_data(current_user: int = Depends(get_current_user)):
    """get_home_data is an endpoint that retrieves the home page data for a user.

    Returns:
        HomeData: A Pydantic model containing the home page data, including the current day, mileage, pace, stimuli, goal RPE, and upcoming workout.
    """
    try:
        # Get the day of the week. Not sure how to store this, since it's updated only when
        # postrun survey is called.

        day_of_week = datetime.now().strftime("%A, %B %-d")

        # Get a user from the database
        retrieved_user = populate_user_info(current_user)

        # Retrieve the current and next day from the user's day_future queue
        current_day = retrieved_user.day_future.get() if retrieved_user.day_future else None
        next_day = retrieved_user.day_future.queue[0] if retrieved_user.day_future and retrieved_user.day_future.qsize(
        ) > 1 else None

        pace_str = ""

        workout_cur = workout_database.get_workout_type_trio(current_day.workouts[0]) if (len(current_day.workouts) == 1) else workout_database.get_workout_type_trio(
            current_day.workouts[0]) + " + \n" + workout_database.get_workout_type_trio(current_day.workouts[1])
        workout_next = workout_database.get_workout_type_trio(next_day.workouts[0]) if (len(next_day.workouts) == 1) else workout_database.get_workout_type_trio(
            next_day.workouts[0]) + " + " + workout_database.get_workout_type_trio(next_day.workouts[1])

        workout_check = workout_database.get_workout_type_trio(
            current_day.workouts[0])
        workout_type_number = user.txt_to_workout_type(workout_check)

        pace = retrieved_user.pace_estimates[workout_type_number] if workout_type_number != -1 else 0

        total_time_current = to_str(round(pace * current_day.total_mileage)) + \
            "-" + to_str(round((pace + 30) * current_day.total_mileage))

        upcoming_workout_check = workout_database.get_workout_type_trio(
            next_day.workouts[0])
        # print(upcoming_workout_check)
        upcoming_workout_type_num = user.txt_to_workout_type(
            upcoming_workout_check)
        # print(upcoming_workout_type_num)
        upcoming_pace = retrieved_user.pace_estimates[
            upcoming_workout_type_num] if upcoming_workout_type_num != -1 else 0
        # print(upcoming_pace)
        upcoming_time = to_str(round(upcoming_pace * next_day.total_mileage)) + \
            "-" + to_str(round((upcoming_pace + 30) * next_day.total_mileage))
        # print(upcoming_time)
        pace_str = to_str(pace) + "-" + \
            to_str(pace + 30) if pace != 0 else ""

        # Get the weeks
        week_id = []
        weekmileage = []
        weekpctcomplete = []
        week_stimuli = []

        for i in range(3):
            current_week = retrieved_user.week_future.queue[i]
            week_id.append(current_week.week_id + 1)
            weekmileage.append(current_week.total_mileage)
            weekpctcomplete.append(current_week.completed_mileage /
                                   current_week.total_mileage if current_week.total_mileage > 0 else 0)
            week_stimuli.append(current_week.cycle)

        return HomeData(
            day=day_of_week,
            mileage=current_day.total_mileage,
            pace=pace_str,
            stimuli=workout_cur,
            goal_rpe=str(current_day.expected_rpe) + "/10",
            # Placeholder time, should be replaced with actual logic based on the user
            time=total_time_current,
            upcoming=workout_next,
            upcomingmileage=next_day.total_mileage,
            # Placeholder time, should be replaced with actual logic based on the user
            upcomingtime=upcoming_time,
            # Could have some issues but for beginning this is fine
            weeknum=week_id,
            weekmileage=weekmileage,
            weekpctcomplete=weekpctcomplete,
            weekstimuli=week_stimuli
        )
    except Exception as e:
        # surface errors as HTTP 500
        logger.exception(
            "Unexpected error in /home/data with user_id=%r", current_user)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/auth/signup", response_model=AuthOut)
async def signup(payload: SignupIn):
    """ signup is an endpoint that handles user signup.

    Args:
        payload (SignupIn): A Pydantic model that contains the user's signup information, including email, username, and password.

    Raises:
        HTTPException: If an error occurs during the signup process, an HTTPException is raised with a status code of 500 and the error message.

    Returns:
        AuthOut: An authorization output model containing the user ID if the signup is successful, or an error code if the username/email already exists.
    """
    try:
        logger.debug(
            "Signup attempt for username=%s email=%s", payload.username, payload.email
        )
        dict = payload.model_dump()
        bool, userid_or_error_code = user_creation.user_exists(dict)
        dict['password'] = user_creation.hash_password(dict['password'])

        if not bool:
            send_user_creds(
                userid_or_error_code, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"], dict)
            logger.debug("User created with user_id=%s", userid_or_error_code)
            return AuthOut(user_id=userid_or_error_code)

        else:
            logger.debug(
                "Signup rejected for username=%s error_code=%s",
                payload.username,
                userid_or_error_code,
            )
            return AuthOut(error_code=userid_or_error_code)
        # Error code 0 indicates the username exists
        # Error code 1 indicates the email exists

    except Exception as e:
        # surface errors as HTTP 500, but log the errors somewhere
        logger.exception(
            "Unexpected error in /auth/signup with payload=%r", payload
        )
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/auth/login", response_model=AuthOut)
async def login(payload: LoginIn, request: Request, response: Response):
    """ login is an endpoint that handles user login.

    Args:
        payload (LoginIn): A Pydantic model that contains the user's login information, including username and password.

    Raises:
        HTTPException: If the credentials are invalid, an HTTPException is raised with a status code of 401. If any other error occurs during the login process, an HTTPException is raised with a status code of 500 and the error message.

    Returns:
        AuthOut: A Pydantic model containing the user ID of the logged-in user.
    """
    ip = request.client.host if request.client else "unknown"
    logger.debug(
        "Login attempt for username=%s from %s", payload.username, ip
    )
    record = LOGIN_ATTEMPTS.get(ip, {"count": 0, "time": time()})
    if time() - record["time"] > BLOCK_TIME:
        record = {"count": 0, "time": time()}
    if record["count"] >= MAX_ATTEMPTS:
        raise HTTPException(
            status_code=429,
            detail="Too many login attempts, try again later.")

    try:
        dict = payload.model_dump()
        userid = user_creation.credential_check(
            dict["username"], dict["password"])
        if userid == 0:
            record["count"] += 1
            LOGIN_ATTEMPTS[ip] = record
            logger.warning(
                "Failed login for username=%s from %s", payload.username, ip
            )
            return AuthOut(error_code=1)

        LOGIN_ATTEMPTS.pop(ip, None)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(userid, access_token_expires)
        refresh_token = create_refresh_token(userid)
        response.set_cookie(
            key="token",
            value=access_token,
            httponly=True,
            max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            samesite="lax",
        )
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            max_age=REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60,
            samesite="lax",
        )
        logger.debug("User %s logged in", payload.username)
        return AuthOut(user_id=userid)
    except Exception as e:
        logger.exception(
            "Unexpected error in /auth/login for username=%s", payload.username)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/auth/refresh", response_model=AuthOut)
async def refresh(response: Response, refresh_token: str | None = Cookie(None)):
    """Refresh the access token using a rotating refresh token."""
    try:
        if not refresh_token:
            raise HTTPException(status_code=401, detail="Missing refresh token")
        user_id, new_refresh = rotate_refresh_token(refresh_token)
        access_token = create_access_token(user_id)
        response.set_cookie(
            key="token",
            value=access_token,
            httponly=True,
            max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            samesite="lax",
        )
        response.set_cookie(
            key="refresh_token",
            value=new_refresh,
            httponly=True,
            max_age=REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60,
            samesite="lax",
        )
        return AuthOut(user_id=user_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Unexpected error in /auth/refresh")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/ping")
async def ping():
    return {"ok": True}
