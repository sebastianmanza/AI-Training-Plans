import pandas as pd

from backend.src.utils.workout.single_workout import single_workout
from backend.src.utils.workout.workout_database import workout_database


xlsx = pd.ExcelFile("backend/data/raw/workouts_to_database.xlsx")

sheet1 = xlsx.parse(0)

# print(sheet1)

new_workout_database = workout_database()
workouts = []
for idx, row in sheet1.iterrows(): # For each row
    trio, reps, pace = [], [], []
    distance = 0
    for col in sheet1.columns: # For each column
        if col == "Trio": # If it's a trio
            for coordinate in str.split(row[col], ","): # Split the item and append each part
                trio.append(int(coordinate))
        elif col == "Reps": # 
            for rep in str.split(row[col], ","):
                reps.append(int(rep.strip()))
        elif col == "Pace":
            pce = str.split(row[col], " ")
            for p in pce:
                pace.append(p.strip())
        else:
            distance = row[col]
    workout = single_workout(workout_database.create_trio(
        trio[0], trio[1], trio[2]), reps, pace, distance)
    new_workout_database.add_workout(workout)
# new_workout_database.print_workouts("Warmup and Cooldown")
# new_workout_database.print_workouts("Kenyan")
new_workout_database.get_individual_workout(4, 5, 6)
