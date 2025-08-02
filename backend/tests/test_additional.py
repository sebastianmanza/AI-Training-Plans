import types
import sys
import importlib
from collections import namedtuple

import pytest

cfg = types.ModuleType('backend.src.utils.SQLutils.config')
cfg.DB_CREDENTIALS = {}
sys.modules['backend.src.utils.SQLutils.config'] = cfg

from backend.src.utils.user_storage.day_plan import day_plan
from backend.src.utils.user_storage.week_plan import week_plan
from backend.src.utils.user_storage.month_plan import month_plan
from backend.src.utils.workout.workout_database import workout_database
from backend.src.utils.workout.workout_storage import workout_storage
from backend.src.utils.workout.single_workout import single_workout
from backend.src.utils.SQLutils.user_retrieve import (
    convert_trio_type_to_tuples,
    convert_trio_types_to_tuples,
)


def test_day_plan_add_and_equality():
    w1 = workout_database.create_trio(1, 1, 1)
    w2 = workout_database.create_trio(3, 5, 2)
    d1 = day_plan(workouts=[w1, w2], total_mileage=5, day_id=1)
    # goal stimuli aggregates max stim/rpe and total distance
    assert d1.goal_stimuli == workout_database.create_trio(3, 5, 3)
    d2 = day_plan(workouts=[w1, w2], total_mileage=5, day_id=1)
    assert d1 == d2
    d1.add_workouts(workout_database.create_trio(2, 2, 1))
    assert len(d1.workouts) == 3
    d2.update__real_rpe(7)
    assert d1 != d2
    assert 'day_id' in repr(d1)


def test_week_plan_add_update_and_equality():
    trio = workout_database.create_trio(1, 2, 3)
    d1 = day_plan(workouts=[trio], total_mileage=3, real_rpe=4)
    d1.update_day(3,4)
    d2 = day_plan(workouts=[trio], total_mileage=3, real_rpe=4)
    d2.update_day(3,4)
    class DummyMonth:
        def __init__(self):
            self.updated = False
        def update_monthly_mileage(self):
            self.updated = True
    m = DummyMonth()
    w = week_plan(total_mileage=3, days=[d1], week_id=1, month_id=m)
    w.add_days([d2])
    assert len(w.days) == 2
    w.update_week()
    assert w.completed_mileage == 3
    assert w.real_rpe == 4
    assert w.percent_completion == 1
    assert m.updated
    w2 = week_plan(total_mileage=3, days=[d1, d2], week_id=1, month_id=m)
    w2.completed_mileage = 3
    w2.real_rpe = 4
    w2.percent_completion = 1
    assert w == w2
    assert 'week_id' in repr(w)


def test_month_plan_add_weeks_percent_and_equality():
    w1 = week_plan(total_mileage=5)
    mp = month_plan(month_id=1, total_mileage=10, weeks=[w1])
    w2 = week_plan(total_mileage=5)
    mp.add_weeks([w2])
    assert len(mp.weeks) == 2
    with pytest.raises(TypeError):
        mp.add_weeks(['not_a_week'])
    mp.completed_mileage = 5
    mp.update_monthly_percent()
    assert mp.percent_completion == 0.5
    mp2 = month_plan(month_id=1, total_mileage=10, weeks=[w1, w2])
    mp2.completed_mileage = 5
    mp2.percent_completion = 0.5
    assert mp == mp2
    assert 'month_id' in repr(mp)


def test_convert_trio_helpers():
    Trio = namedtuple('trio', 'stim rpe dist')
    trios = [Trio(1,2,3), Trio(4,5,6)]
    assert convert_trio_types_to_tuples(trios) == [(1,2,3),(4,5,6)]
    assert convert_trio_type_to_tuples(Trio(7,8,9)) == (7,8,9)
    assert convert_trio_type_to_tuples(None) == (0.0,0.0,0.0)


def test_cast_workouts_to_trios():
    cfg = types.ModuleType('backend.src.utils.SQLutils.config')
    cfg.DB_CREDENTIALS = {}
    sys.modules['backend.src.utils.SQLutils.config'] = cfg
    from backend.src.utils.SQLutils import user_send
    Trio = namedtuple('trio', 'stim rpe dist')
    assert user_send.cast_workouts_to_trios([(1,2,3)], Trio) == [Trio(1,2,3)]


def test_database_connect_helpers(monkeypatch):
    # provide stub config
    cfg = types.ModuleType('backend.src.utils.SQLutils.config')
    cfg.DB_CREDENTIALS = {'host': 'h'}
    sys.modules['backend.src.utils.SQLutils.config'] = cfg
    dbc = importlib.reload(importlib.import_module('backend.src.utils.SQLutils.database_connect'))

    class DummyCursor:
        def __init__(self, result=None, fail=False):
            self.result = result
            self.fail = fail
            self.executed = None
        def execute(self, query, params):
            if self.fail:
                raise dbc.psycopg2.Error()
            self.executed = (query, params)
        def fetchall(self):
            return self.result

    cur = DummyCursor([(1,)])
    assert dbc.db_select(cur, 'Q', 1) == [(1,)]
    cur_fail = DummyCursor(fail=True)
    assert dbc.db_select(cur_fail, 'Q', 1) is None

    cur2 = DummyCursor()
    dbc.db_insert(cur2, 1,'dob','sex','ex',0,0,0,'2025-01-01','pace','days',1,'{}')
    assert 'INSERT INTO public.userlistai' in cur2.executed[0]
    cur3 = DummyCursor()
    dbc.db_update(cur3, 1,'dob','sex','ex',0,0,0,'2025-01-01','pace','days',1,'{}')
    assert 'UPDATE public.userlistai' in cur3.executed[0]

    def fail_connect(*a, **k):
        raise dbc.psycopg2.Error()
    monkeypatch.setattr(dbc.psycopg2, 'connect', fail_connect)
    assert dbc.init_db('u','p') is None


def test_workout_database_mass_add(monkeypatch):
    # reset global storage
    monkeypatch.setattr(workout_database, 'storage', workout_storage())
    db = workout_database()
    t1 = workout_database.create_trio('2.5','4','5.5')
    w1 = single_workout(t1, [], [], 0)
    db.add_workout(w1)
    assert db.easyrun[0] is w1
    t2 = workout_database.create_trio(2,3,4.5)
    w2 = single_workout(t2, [], [], 0)
    db.mass_add_workouts([w2])
    assert db.recovery[0] is w2
    assert db.get_individual_workout(2.5,4,5.5) is w1
    assert workout_database.workout_trio_equal(w1, w1)
