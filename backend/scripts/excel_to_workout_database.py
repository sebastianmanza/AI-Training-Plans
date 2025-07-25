import pandas as pd

from backend.src.utils.workout.single_workout import single_workout
from backend.src.utils.workout.workout_database import workout_database


xlsx = pd.ExcelFile("backend/data/raw/workouts_to_database.xlsx")

sheet1 = xlsx.parse(0)
TRIO_STIM, TRIO_RPE, TRIO_DIST = 0, 1, 2  # Constants for indexing the trio

# print(sheet1)

new_workout_database = workout_database()
workouts = []
for idx, row in sheet1.iterrows():  # For each row
    trio, reps, pace = [], [], []
    distance = 0
    for col in sheet1.columns:  # For each column
        if col == "Trio":  # If it's a trio
            # Split the item and append each part
            for coordinate in str(row[col]).split(","):
                trio.append(float(coordinate))
            for rep in str(row[col]).split(","):
                reps.append(float(rep.strip()))
            for pac in str(row[col]).split(" "):
                pace.append(pac.strip())
        else:
            distance = row[col]

    workouts.append(single_workout
                    (workout_database.create_trio(trio[TRIO_STIM], trio[TRIO_RPE], trio[TRIO_DIST]), reps, pace, distance))
workouts = sorted(workouts, key=lambda x: (
    x.get_stim(), x.get_rpe(), x.get_distance()))

def get_workout_list():
    return workouts

new_workout_database.mass_add_workouts(workouts)
new_workout_database.print_workouts("Warmup and Cooldown")
new_workout_database.print_workouts("Easy Run")
new_workout_database.print_workouts("Progression")
new_workout_database.print_workouts("Recovery Run")
