import math
import pytest

from backend.src.utils import RPEutils as rpe
from backend.src.utils import pace_calculations as pace
from backend.src.utils.user_storage.day_plan import day_plan
from backend.src.utils.user_storage.week_plan import week_plan
from backend.src.utils.user_storage.month_plan import month_plan
from backend.src.utils.user_storage.training_database import training_database
from backend.src.utils.user_storage.storage_stacks_and_queues import (
    storage_stacks_and_queues,
)
from backend.src.utils.workout.workout_database import workout_database
from backend.src.utils.workout.workout_storage import workout_storage
from backend.src.utils.workout.single_workout import single_workout
from backend.src.utils.user_creation import validate_address

# ``user`` imports optional database utilities.  During testing the database
# stack may not be installed, so fall back to a ``None`` sentinel and skip user
# specific tests if the import fails.
try:  # pragma: no cover - best effort import
    from backend.src.utils.user_storage.user import user, EASY, FIVEK
except Exception:  # pragma: no cover
    user = None
    EASY = FIVEK = 0


def test_rpeutils_completion_score():
    score = rpe.completion_score(5, 4, 8, 7)
    assert math.isclose(score, -0.2625, rel_tol=1e-4)

def test_rpeutils_delta_rpe():
    assert rpe.delta_RPE(7, 6) == -1

def test_rpeutils_delta_difficulty():
    assert math.isclose(rpe.delta_difficulty(0.5, 0.2), 0.4)


def test_rpeutils_edge_cases():
    """Edge cases for RPE utilities."""
    with pytest.raises(ZeroDivisionError):
        rpe.completion_score(0, 1, 1, 1)
    assert rpe.delta_difficulty(0.2, -1) == 0.2 - (-1) * 0.5


def test_pace_to_from_str():
    assert pace.to_str(125) == "2:05"
    assert pace.from_str("2:05") == 125


def test_pace_time_edge_cases():
    assert pace.to_str(0) == "00"
    assert pace.from_str("1:02:03") == 3723


def test_pace_from_dec():
    assert pace.from_dec(7.5) == "7:30"


def test_total_time_functions():
    assert pace.total_time_miles(480, 3) == 1439
    assert pace.total_time(480, 1609) == 479
    assert pace.mile_pace(480, 1600) == 482
    assert pace.total_time(480, 0) == 0
    assert pace.mile_pace(480, 0) == 0


def test_get_vdot():
    assert pace.get_VDOT(5000, 1500) > 0
    with pytest.raises(ValueError):
        pace.get_VDOT(-1, 1500)
    with pytest.raises(ValueError):
        pace.get_VDOT(1000, 0)


def test_average_property():
    class Obj:
        def __init__(self, val):
            self.val = val
    assert pace.average_property([Obj(1), Obj(3)], "val") == 2


def test_average_property_missing():
    class Obj:
        def __init__(self):
            self.other = 1
    with pytest.raises(ValueError):
        pace.average_property([Obj()], "val")


def test_average_property_empty():
    assert pace.average_property([], "val") == 0


def test_day_plan_update():
    trio = workout_database.create_trio(1, 1, 1)
    d = day_plan(workouts=[trio], total_mileage=10, expected_rpe=5)
    d.update_day(5, 6)
    assert d.completed_mileage == 5
    assert d.real_rpe == 6
    assert d.percent_completion == 0.5


def test_day_plan_zero_mileage():
    trio = workout_database.create_trio(1, 1, 1)
    d = day_plan(workouts=[trio], total_mileage=0)
    d.update_day(0, 0)
    assert d.percent_completion == 1


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


def test_week_plan_zero_total_mileage():
    w = week_plan(total_mileage=0, days=[])
    w.update_weekly_percent()
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
    if user is None:
        pytest.skip("user module not available")

    u = user(
        dob="2000-01-01",
        sex="M",
        running_ex="Advanced",
        injury=0,
        most_recent_injury=0,
        longest_run=10,
        goal_date="2026-01-01",
        available_days=[1, 1, 1, 1, 1, 1, 1],
        number_of_days=7,
        pace_estimates=[-1] * 10,
    )

    u.set_5k_pace("6:00")
    assert u.get_pace(1) != -1  # FIVEK index is 1 per constants
    assert u.modify_pace(10, 1) == u.pace_estimates[1] + 10
    assert user.txt_to_workout_type("Easy Run") == 4  # EASY constant
    assert user.txt_to_workout_type("Unknown") == -1

    v = user(
        dob="2000-01-01",
        sex="M",
        running_ex="Advanced",
        injury=0,
        most_recent_injury=0,
        longest_run=10,
        goal_date="2026-01-01",
        available_days=[1, 1, 1, 1, 1, 1, 1],
        number_of_days=7,
        pace_estimates=[-1] * 10,
    )
    with pytest.raises(ValueError):
        v.get_training_pace(0)


def test_pace_training_helper_and_string_inputs():
    assert pace.get_training_pace_helper(5000, 17 * 60 + 30, 0.62) > 0
    assert pace.total_time_miles("8:00", 2) == 960
    assert pace.total_time("8:00", 1600) == 477


def test_user_rpe_and_predictions():
    if user is None:
        pytest.skip("user module not available")

    u = user(
        dob="2000-01-01",
        sex="M",
        running_ex="Advanced",
        injury=0,
        most_recent_injury=0,
        longest_run=10,
        goal_date="2026-01-01",
        available_days=[1, 1, 1, 1, 1, 1, 1],
        number_of_days=7,
        pace_estimates=[-1] * 10,
    )

    u.update_mean_RPE("Easy Run", 5, 4)
    assert math.isclose(u.get_type_mean_RPE("Easy Run"), 5)
    assert math.isclose(u.get_type_deviation_RPE("Easy Run"), 1)

    u.set_5k_pace("6:00")
    u.make_predictions()
    assert all(p >= 0 for p in u.pace_estimates)
    assert u.get_times().count("\n") == len(u.pace_estimates)

    uid = u.get_user_id()
    assert u.get_user_id() == uid
    assert isinstance(u.get_age(), int)

    u.append_month("m")
    u.append_week("w")
    u.append_day("d")
    assert u.month_history[-1] == "m"
    assert u.week_history[-1] == "w"
    assert u.day_history[-1] == "d"

    u.append_fut_month("fm")
    u.append_fut_week("fw")
    u.append_fut_day("fd")
    assert u.month_future.get() == "fm"
    assert u.week_future.get() == "fw"
    assert u.day_future.get() == "fd"

    with pytest.raises(RuntimeError):
        user.user_id_exists(uid)

    new_id = user.generate_new_id()
    assert 10000000 <= new_id < 100000000
    assert str(uid) in repr(u)


def test_validate_address():
    assert validate_address("valid@example.com")
    assert not validate_address("invalid-email")


def test_storage_stacks_and_queues_init():
    s = storage_stacks_and_queues()
    assert len(s.month_history) == len(s.week_history) == len(s.day_history) == 0
    assert s.month_future.empty() and s.week_future.empty() and s.day_future.empty()


def test_training_database_singleton():
    db1 = training_database()
    db2 = training_database.get_instance()
    db3 = training_database()
    assert db1 is db2 is db3
    assert db1.day is db1.storage.day_future


def test_workout_storage_getters_reference_lists():
    ws = workout_storage()
    er = ws.get_easyrun_workouts()
    assert er == []
    er.append("w")
    assert ws.easyrun == ["w"]


def test_user_training_pace_requires_prediction():
    if user is None:
        pytest.skip("user module not available")

    u = user(
        dob="2000-01-01",
        sex="M",
        running_ex="Advanced",
        injury=0,
        most_recent_injury=0,
        longest_run=10,
        goal_date="2026-01-01",
        available_days=[1] * 7,
        number_of_days=7,
        pace_estimates=[-1] * 10,
    )

    with pytest.raises(ValueError):
        u.get_training_pace(EASY)


def test_user_equality_and_modify_pace():
    if user is None:
        pytest.skip("user module not available")

    base = dict(
        dob="2000-01-01",
        sex="M",
        running_ex="Advanced",
        injury=0,
        most_recent_injury=0,
        longest_run=10,
        goal_date="2026-01-01",
        available_days=[1] * 7,
        number_of_days=7,
        user_id=12345678,
    )
    u1 = user(pace_estimates=[300] * 10, **base)
    u2 = user(pace_estimates=[300] * 10, **base)
    assert u1 == u2

    u1.set_5k_pace(310)
    assert u1 != u2

    original = u1.get_pace(FIVEK)
    assert u1.modify_pace(-5, FIVEK) == original - 5
    assert u1.get_pace(FIVEK) == original

