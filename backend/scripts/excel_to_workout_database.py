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
            for coordinate in str.split(row[col], ","):
                trio.append(int(coordinate))
        elif col == "Reps":
            for rep in str.split(row[col], ","):
                reps.append(int(rep.strip()))
        elif col == "Pace":
            for pac in str.split(row[col], " "):
                pace.append(pac.strip())
        else:
            distance = row[col]

    workouts.append(single_workout
                    (workout_database.create_trio(trio[TRIO_STIM], trio[TRIO_RPE], trio[TRIO_DIST]), reps, pace, distance))
workouts = sorted(workouts, key=lambda x: (
    x.get_stim(), x.get_rpe(), x.get_distance()))

new_workout_database.mass_add_workouts(workouts)
new_workout_database.print_workouts("Warmup and Cooldown")
new_workout_database.print_workouts("Progression")
