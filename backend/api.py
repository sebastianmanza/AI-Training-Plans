from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
