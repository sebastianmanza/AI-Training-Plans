from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, date

from backend.scripts.txt_to_database import txt_to_database
from backend.src.main.frontend_compatible_survey import main as SurveyMain

app = FastAPI()

# Allow simulator to find API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SurveyIn(BaseModel):
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


@app.post("/survey/prelim")
async def survey_prelim(payload: SurveyIn):
    try:
        # dispatch to your pure‐function—no input(), no print()
        result = SurveyMain.prelim_survey(payload.model_dump())
        return result
    except Exception as e:
        # surface errors as HTTP 500
        raise HTTPException(status_code=500, detail=str(e))
    
class HomeData(BaseModel):
    day: str               # e.g. "MONDAY"
    mileage: float           # e.g. 7
    pace: str              # e.g. "7:00-7:30"
    stimuli: str           # trio here (for now), this will eventually be workout type. If workout is multiple, it will look like "workout1 + workout2"
    goal_rpe: str          # e.g. "5/10"
    upcoming: str          # e.g. "3 MILE KENYAN" // next days workout type
    
@app.get("/home/data", response_model=HomeData)
async def get_home_data():
    cur_day = datetime.now().strftime("%A")
    
    # TODO Replace with actual retrieval using user_id in the SQL database
    # For now, we will use a placeholder for our training plans
    database = txt_to_database("backend/data/raw/training_plan_test.txt")
    current_day_object = database.day.get()
    next_day = database.day.get()
    
    
    return HomeData(
        day = cur_day,
        mileage = current_day_object.total_mileage,
        pace= "7:00-7:30",  # Placeholder pace, should be replaced with actual logic
        stimuli = "EASY RUN",
        goal_rpe = str(current_day_object.expected_rpe) + "/10",
        upcoming = "3 MILE KENYAN"
    )
