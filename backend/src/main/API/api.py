from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import logging
from logging.handlers import RotatingFileHandler

from backend.scripts.txt_to_database import txt_to_database
from backend.src.utils import user_creation
from backend.src.utils.workout.workout_database import workout_database
from backend.src.main.API.initial_user_to_sql import main as SurveyMain
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.SQLutils.user_send import send_user_info
from backend.src.utils.SQLutils.user_retrieve import populate_user_info
from backend.src.utils.user_storage.user import user
from backend.src.utils.pace_calculations import to_str

handler = RotatingFileHandler(
    filename="app_errors.log",
    maxBytes=5 * 1024 * 1024,
    backupCount=3,
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s [%(name)s] %(message)s"
)
handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(handler)


app = FastAPI()

# Allow simulator to find API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SurveyIn(BaseModel):
    """SurveyIn is a Pydantic model that represents the input for the preliminary survey.
    """
    user_id: int
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
    day: str               # e.g. "MONDAY"
    mileage: float           # e.g. 7
    pace: str              # e.g. "7:00-7:30"
    # trio here (for now), this will eventually be workout type. If workout is multiple, it will look like "workout1 + workout2"
    stimuli: str
    goal_rpe: str          # e.g. "5/10"
    upcoming: str          # e.g. "3 MILE KENYAN" // next days workout type


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
async def survey_prelim(payload: SurveyIn):
    """survey_prelim is an endpoint that handles the preliminary survey for a user.

    Args:
        payload (SurveyIn): A Pydantic model that contains the user's responses to the preliminary survey.

    Raises:
        HTTPException: If an error occurs during the processing of the survey, an HTTPException is raised with a status code of 500 and the error message.

    Returns:
        str: A string containing the status of the survey submission, typically an acknowledgment of successful processing.
    """
    try:
        # dispatch to your pure‐function—no input(), no print()
        result = SurveyMain.prelim_survey(payload.model_dump())
        print(result)
        return result
    except Exception as e:
        # surface errors as HTTP 500 and log to the log file
        logging.exception("Unexpected error in /survey/prelim with payload=%r", payload)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/post_run_survey")
async def post_run_survey(payload: Post_Run_SurveyIn):
    """post_run_survey is an endpoint that handles the post run survey of a user

    Args:
        payload (Post_Run_SurveyIn): A Pydantic model that contains the user's responses to the preliminary survey.
    
    Raises:
        HTTPException: If an error occurs during the processing of the survey, an HTTPException is raised with a status code of 500 and the error message.

    Returns:
        str: A string containing the status of the survey submission, typically an acknowledgment of successful processing.
    """
    try:
        result = SurveyMain.post_run_survey(payload.model_dump())
        # dispatch to your pure‐function—no input(), no print()
        print(result)
        return result
    except Exception as e:
         # surface errors as HTTP 500
        raise HTTPException(status_cdoe=500, detail=str(e))

@app.get("/home/data", response_model=HomeData)
async def get_home_data(user_id: int = 0):

    """get_home_data is an endpoint that retrieves the home page data for a user.

    Args:
        user_id (int): The ID of the user for whom the home page data is being retrieved.

    Returns:
        HomeData: A Pydantic model containing the home page data, including the current day, mileage, pace, stimuli, goal RPE, and upcoming workout.
    """
    try:
        day_of_week = datetime.now().strftime("%A")

        retrieved_user = populate_user_info(user_id)

        current_day = retrieved_user.day_future.get() if retrieved_user.day_future else None
        next_day = retrieved_user.day_future.queue[0] if retrieved_user.day_future and retrieved_user.day_future.qsize(
        ) > 1 else None

        pace_str = ""

        # Create a string representation of the current day and next day workouts
        # print(current_day.workouts)
        # print(current_day.workouts[3])
        workout_cur = workout_database.get_workout_type_trio(current_day.workouts[0]) if (len(current_day.workouts) == 1) else workout_database.get_workout_type_trio(
            current_day.workouts[0]) + " + \n" + workout_database.get_workout_type_trio(current_day.workouts[1])
        workout_next = workout_database.get_workout_type_trio(next_day.workouts[0]) if (len(next_day.workouts) == 1) else workout_database.get_workout_type_trio(
            next_day.workouts[0]) + " + " + workout_database.get_workout_type_trio(next_day.workouts[1])

        workout_check = workout_database.get_workout_type_trio(
            current_day.workouts[0])
        pace = retrieved_user.pace_estimates[user.txt_to_workout_type(
            workout_check)] if workout_check in retrieved_user.pace_estimates else 0

        pace_str = to_str(pace) + "-" + to_str(pace + 30) if pace != 0 else ""

        return HomeData(
            day=day_of_week,
            mileage=current_day.total_mileage,
            pace=pace_str,  # Placeholder pace, should be replaced with actual logic based on the user
            stimuli=workout_cur,
            goal_rpe=str(current_day.expected_rpe) + "/10",
            upcoming=workout_next
        )
    except Exception as e:
        # surface errors as HTTP 500
        logging.exception(
            "Unexpected error in /home/data with user_id=%r", user_id)
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
        dict = payload.model_dump()
        bool, userid_or_error_code = user_creation.user_exists(dict)
        # Hash the password before sending it to the database
        dict['password'] = hash(dict['password'])

        if not bool:
            user_creation.send_user_creds(
                userid_or_error_code, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"], dict)
            # return the userid to the session
            print(userid_or_error_code)
            return AuthOut(user_id = userid_or_error_code)

        else:
            return AuthOut(error_code=userid_or_error_code)
        # Error code 0 indicates the username exists
        # Error code 1 indicates the email exists

    except Exception as e:
        # surface errors as HTTP 500, but log the goddamn errors somewhere
        logging.exception(
            "Unexpected error in /auth/signup with payload=%r", payload)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/auth/login", response_model=AuthOut)
async def login(payload: LoginIn):
    """ login is an endpoint that handles user login.

    Args:
        payload (LoginIn): A Pydantic model that contains the user's login information, including username and password.

    Raises:
        HTTPException: If the credentials are invalid, an HTTPException is raised with a status code of 401. If any other error occurs during the login process, an HTTPException is raised with a status code of 500 and the error message.

    Returns:
        AuthOut: A Pydantic model containing the user ID of the logged-in user.
    """
    try:
        dict = payload.model_dump()
        userid = user_creation.credential_check(
            dict["username"], dict["password"])
        if userid == 0:
            # Error code 1 indicates invalid credentials
            return AuthOut(error_code=1)

        return AuthOut(user_id=userid)
    except Exception as e:
        # surface errors as HTTP 500
        logging.exception(
            "Unexpected error in /auth/login with payload=%r", payload)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/ping")
async def ping():
    return {"ok": True}
