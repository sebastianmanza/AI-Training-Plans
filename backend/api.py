from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, date

from backend.scripts.txt_to_database import txt_to_database
from backend.src.utils.workout.workout_database import workout_database
from backend.src.main.frontend_compatible_survey import main as SurveyMain
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.SQLutils.user_send import send_user_info
# from backend.src.utils import user_creation
from backend.src.utils.SQLutils.user_retrieve import populate_user_info
from backend.src.utils.user_storage.user import user
from backend.src.utils.time_conversion import to_str

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
    date_of_birth: str
    sex: str
    running_experience: str
    days_per_week: int
    days_of_week: list
    most_time_day: str
    current_5k_fitness: int
    major_injuries: str
    most_recent_injury: str

# Endpoint for preliminary survey
    
class HomeData(BaseModel):
    """HomeData is a Pydantic model that represents the data returned for the home page.
    """
    day: str               # e.g. "MONDAY"
    mileage: float           # e.g. 7
    pace: str              # e.g. "7:00-7:30"
    stimuli: str           # trio here (for now), this will eventually be workout type. If workout is multiple, it will look like "workout1 + workout2"
    goal_rpe: str          # e.g. "5/10"
    upcoming: str          # e.g. "3 MILE KENYAN" // next days workout type
 
class SignupIn(BaseModel):
    """SignupIn is a Pydantic model that represents the input for user signup.
    """
    email: str
    username: str
    password: str
    survey: dict  
    
class LoginIn(BaseModel):
    """LoginIn is a Pydantic model that represents the input for user login.
    """
    username: str
    password: str 
    
class AuthOut(BaseModel):
    """AuthOut is a Pydantic model that represents the output for user authentication (login and signup)
    """
    user_id: int

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
        return result
    except Exception as e:
        # surface errors as HTTP 500
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/home/data", response_model=HomeData)
async def get_home_data(user_id: int = 0):
    """get_home_data is an endpoint that retrieves the home page data for a user.

    Args:
        user_id (int): The ID of the user for whom the home page data is being retrieved.

    Returns:
        HomeData: A Pydantic model containing the home page data, including the current day, mileage, pace, stimuli, goal RPE, and upcoming workout.
    """
    day_of_week = datetime.now().strftime("%A")
    
    # user = populate_user_info(user_id)
    
    # current_day = user.day_future.get() if user.day_future else None
    # next_day = user.day_future.queue[0] if user.day_future and len(user.day_future) > 1 else None
    
    
    
    # TODO Replace with actual retrieval using user_id in the SQL database
    # Logic should go something like this: 
        # 1. Retrieve user_id from session (either logged in user or when user logs in)
        # 2. Use user_id to retrieve the whole user from the database
        # 3. For now use the assumption that the user is filling out post run everyday, update the stack with the info entered
        # 4. put that on the stack, pop the top of the stack and shift everything into their places
        # 5. send info back to the database
        
        
    # For now, we will use a placeholder for our training plans
    database = txt_to_database("backend/data/raw/training_plan_test.txt")
    test_user = user("3/17/2005", sex = "Male", running_ex="Advanced", five_km_estimate="15:10", goal_date=date(2024, 5, 1), mean_RPE=5, STD_RPE=2)
    test_user.day_future = database.day
    test_user.week_future = database.week
    test_user.month_future = database.month
    
    current_day = test_user.day_future.get()
    next_day = test_user.day_future.queue[0]
    
    pace = 0
    pace_str = ""
    
    
    # Create a string representation of the current day and next day workouts
    workout_cur = workout_database.get_workout_type_trio(current_day.workouts[0]) if (len(current_day.workouts) == 1) else workout_database.get_workout_type_trio(current_day.workouts[0]) + " + \n" + workout_database.get_workout_type_trio(current_day.workouts[1])
    workout_next = workout_database.get_workout_type_trio(next_day.workouts[0]) if (len(next_day.workouts) == 1) else workout_database.get_workout_type_trio(next_day.workouts[0]) + " + " + workout_database.get_workout_type_trio(next_day.workouts[1])
    
    workout_check = workout_database.get_workout_type_trio(current_day.workouts[0])
    pace = test_user.get_training_pace(workout_check)
        
    pace_str = to_str(pace) + "-" + to_str(pace + 30) if pace != 0 else ""
    
    return HomeData(
        day = day_of_week,
        mileage = current_day.total_mileage,
        pace= pace_str,  # Placeholder pace, should be replaced with actual logic based on the user
        stimuli = workout_cur,
        goal_rpe = str(current_day.expected_rpe) + "/10",
        upcoming = workout_next
    )
    
    
@app.post("/auth/signup", response_model = AuthOut)
async def signup(payload: SignupIn):
    """ signup is an endpoint that handles user signup.

    Args:
        payload (SignupIn): A Pydantic model that contains the user's signup information, including email, username, password, and survey data.

    Raises:
        HTTPException: If an error occurs during the signup process, an HTTPException is raised with a status code of 500 and the error message.

    Returns:
        AuthOut: A Pydantic model containing the user ID of the newly created user.
    """
    try:
        new_user = user_creation.user_create(
            email=payload.email,
            username=payload.username,
            password=payload.password,
            survey=payload.survey
        )
        
        send_user_info(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
        
        return AuthOut(user_id=new_user.user_id)
    except Exception as e:
        # surface errors as HTTP 500
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.post("/auth/login", response_model = AuthOut)
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
        user = user_creation.user_login(
            username=payload.username,
            password=payload.password
        )
        
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return AuthOut(user_id=user.user_id)
    except Exception as e:
        # surface errors as HTTP 500
        raise HTTPException(status_code=500, detail=str(e))
    
