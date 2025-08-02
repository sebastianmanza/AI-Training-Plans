import math
import pytest

from backend.src.utils import RPEutils as rpe
from backend.src.utils import pace_calculations as pace
from backend.src.utils.user_storage.day_plan import day_plan
from backend.src.utils.user_storage.week_plan import week_plan
from backend.src.utils.user_storage.month_plan import month_plan
from backend.src.utils.workout.workout_database import workout_database
from backend.src.utils.workout.single_workout import single_workout
from backend.src.utils.user_storage.user import user


def test_rpeutils_completion_score():
    score = rpe.completion_score(5, 4, 8, 7)
    assert math.isclose(score, -0.2625, rel_tol=1e-4)

def test_rpeutils_delta_rpe():
    assert rpe.delta_RPE(7, 6) == -1

def test_rpeutils_delta_difficulty():
    assert math.isclose(rpe.delta_difficulty(0.5, 0.2), 0.4)


def test_pace_to_from_str():
    assert pace.to_str(125) == "2:05"
    assert pace.from_str("2:05") == 125


def test_pace_from_dec():
    assert pace.from_dec(7.5) == "7:30"


def test_total_time_functions():
    assert pace.total_time_miles(480, 3) == 1439
    assert pace.total_time(480, 1609) == 479
    assert pace.mile_pace(480, 1600) == 482


def test_average_property():
    class Obj:
        def __init__(self, val):
            self.val = val
    assert pace.average_property([Obj(1), Obj(3)], "val") == 2


def test_day_plan_update():
    trio = workout_database.create_trio(1, 1, 1)
    d = day_plan(workouts=[trio], total_mileage=10, expected_rpe=5)
    d.update_day(5, 6)
    assert d.completed_mileage == 5
    assert d.real_rpe == 6
    assert d.percent_completion == 0.5


def test_week_plan_updates():
    trio = workout_database.create_trio(1, 2, 3)
    d = day_plan(workouts=[trio], total_mileage=5)
    d.update_day(5, 6)
    w = week_plan(total_mileage=5, days=[d])
    w.update_weekly_mileage()
    w.update_weekly_real_rpe()
    w.update_weekly_percent()
    assert w.completed_mileage == 5
    assert w.real_rpe == 6
    assert w.percent_completion == 1

# month_plan has a bug where ``update_monthly_mileage`` is nested inside
# ``update_monthly_real_rpe``. Calling ``update_week`` therefore raises
# ``AttributeError``. Once the bug is fixed this test can be enabled as a
# standard assertion.
@pytest.mark.xfail(strict=True, raises=AttributeError)
def test_month_plan_update_bug():
    m = month_plan(weeks=[week_plan()])
    m.update_week()


def test_single_workout_accessors():
    trio = workout_database.create_trio(1, 2, 3)
    w = single_workout(trio, [1, 2], ["5k"], 10)
    assert w.get_trio() == trio
    assert w.get_pace() == ["5k"]
    assert "Workout" in str(w)


def test_workout_database_basic():
    wd = workout_database()
    trio = workout_database.create_trio(2.5, 4, 5.5)
    assert wd.get_workout_type(2.5, 4, 5.5) == "Easy Run"
    assert wd.get_workout_type_trio(trio) == "Easy Run"
    assert wd.get_workout_type_coordinates(2.5, 4, 5.5) == trio
    assert wd.match_execute("Easy Run", lambda l: "ok") == "ok"


def test_user_methods():
    u = user(
        dob="2000-01-01",
        sex="M",
        running_ex="Advanced",
        injury=0,
        most_recent_injury=0,
        longest_run=10,
        goal_date="2026-01-01",
        available_days=[1,1,1,1,1,1,1],
        number_of_days=7,
    )
    # update_mean_RPE currently uses dict.update incorrectly and raises
    # a TypeError. Once fixed these assertions can be re-enabled.
    # u.update_mean_RPE("Easy Run", 5, 4)
    # assert u.get_type_mean_RPE("Easy Run") == 5
    # assert u.get_type_deviation_RPE("Easy Run") == 1
    u.set_5k_pace("6:00")
    assert u.get_pace(1) != -1  # FIVEK index is 1 per constants
    assert u.modify_pace(10, 1) == u.pace_estimates[1] + 10
    assert user.txt_to_workout_type("Easy Run") == 4  # EASY constant

