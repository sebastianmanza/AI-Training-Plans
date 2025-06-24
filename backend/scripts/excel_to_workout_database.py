import pandas as pd

from backend.src.utils.workout.single_workout import single_workout
from backend.src.utils.workout.workout_database import workout_database
from backend.src.utils.workout.workout_type_library import workout_type_library


xlsx = pd.ExcelFile("backend/data/raw/workouts_to_database.xlsx")

sheet1 = xlsx.parse(0)

# print(sheet1)

new_workout_database = workout_database()
workouts = []
for idx, row in sheet1.iterrows():
    trio = []
    reps = []
    pace = []
    distance = 0
    for col in sheet1.columns:
        if col == "Trio":
            lst = str.split(row[col], ",")
            trio.append(int(lst[0]))
            trio.append(int(lst[1]))
            trio.append(int(lst[2]))
        elif col == "Reps":
            rps = str.split(row[col], ",")
            for r in rps:
                reps.append(int(r.strip()))
        elif col == "Pace":
            pce = str.split(row[col], " ")
            for p in pce:
                pace.append(p.strip())
        else:
            distance = row[col]
    workouts.append(single_workout(workout_type_library.create_trio(
        trio[0], trio[1], trio[2]), reps, pace, distance))
workouts = sorted(workouts, key=lambda x: (
    x.get_stim(), x.get_rpe(), x.get_distance()))

new_workout_database.mass_add_workouts(workouts)
new_workout_database.print_workouts("Warmup and Cooldown")
new_workout_database.print_workouts("Kenyan")
