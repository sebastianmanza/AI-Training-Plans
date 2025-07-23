from backend.src.utils.workout.workout_database import workout_database
from backend.scripts.excel_to_workout_database import get_workout_list
from backend.src.utils.workout import single_workout


wd = workout_database()

def test_workout_database():
    workouts = get_workout_list()
    wd.mass_add_workouts(workouts)
    assert wd.get_individual_workout(4, 5, 6) == workouts[2]
    assert wd.get_workout_type(4, 5, 6) == "Progression"
    assert "Progression" == wd.get_workout_type(workouts[2].get_stim(), workouts[2].get_rpe(), workouts[2].get_distance())
    assert wd.get_workout_type_coordinates(4, 5, 6) == wd.create_trio(4, 6, 6)