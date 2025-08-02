import pytest

from backend.src.utils.workout.workout_database import workout_database
from backend.src.utils.workout.single_workout import single_workout


def _sample_workouts():
    """Return a couple of hand crafted workouts for testing."""
    return [
        single_workout(workout_database.create_trio(2.5, 4, 5.5), [1], ["5k"], 10),
        single_workout(workout_database.create_trio(4, 6, 6), [2], ["5k"], 20),
    ]


def test_workout_database_operations():
    wd = workout_database()
    workouts = _sample_workouts()
    wd.mass_add_workouts(workouts)

    assert wd.get_individual_workout(4, 6, 6) == workouts[1]
    assert wd.get_workout_type(4, 6, 6) == "Progression"
    assert wd.get_workout_type_coordinates(2.5, 4, 5.5) == workouts[0].get_trio()
    assert wd.match_execute("Easy Run", lambda lst: len(lst)) >= 1

    with pytest.raises(ValueError):
        wd.get_workout_type(0, 0, 1)

    assert workout_database.get_distance(workouts[0].get_trio(), 2.5, 4, 5.5) == 0
    assert workout_database.workout_trio_equal(workouts[0], workouts[0])
    assert wd.get_workout_type_coordinates(0, 0, 0) == workout_database.create_trio(0, 0, 0)


def test_single_workout_helpers():
    trio1 = workout_database.create_trio(1, 2, 3)
    trio2 = workout_database.create_trio(1, 2, 4)
    w = single_workout(trio1, [1, 2], ["5k"], 10)

    assert single_workout.trio_equal(trio1, trio1)
    assert not single_workout.trio_equal(trio1, trio2)
    assert w.get_stim() == 1
    assert w.get_rpe() == 2
    assert w.get_distance() == 3
    assert w.get_reps() == [1, 2]
    assert "Workout:" in str(w)


def test_workout_database_edge_cases():
    wd = workout_database()
    wd.easyrun.clear()  # ensure a clean slate across tests
    w = single_workout(workout_database.create_trio(2.5, 4, 5.5), [1], ["5k"], 10)
    wd.add_workout(w)

    # create_trio normalizes to floats
    trio = workout_database.create_trio(2, 3, 4)
    assert isinstance(trio[0], float)

    assert wd.get_workout_storage_type("Easy Run") is wd.easyrun
    assert wd.get_individual_workout_helper(2.5, 4, 5.5, "Easy Run") == w
    assert workout_database.get_workout_difference(2.5, 4, 5.5) == (0.0, 0.0, 0.0)

    with pytest.raises(ValueError):
        wd.get_workout_type_coordinates(99, 99, 99)


def test_workout_database_off_and_difference():
    wd = workout_database()
    assert wd.get_workout_type(0, 0, 0) == "Off"
    diff = workout_database.get_workout_difference(3.5, 4, 5.5)
    assert diff == (1.0, 0.0, 0.0)

