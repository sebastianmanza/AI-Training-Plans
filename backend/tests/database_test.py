import secrets
import pathlib
import pytest

# Only run these tests when a database configuration file is present.  This
# mirrors the runtime behaviour of the code which expects optional database
# utilities to exist.  When the configuration is missing the tests are skipped
# rather than failing due to missing credentials or drivers.
if not pathlib.Path("backend/src/utils/SQLutils/config.py").exists():
    pytest.skip("database tests require external dependencies", allow_module_level=True)

from backend.scripts.txt_to_database import txt_to_database  # pragma: no cover
from backend.src.utils.SQLutils.database_connect import init_db, db_select  # pragma: no cover
from backend.src.utils.SQLutils.user_retrieve import convert_trio_types_to_tuples, populate_user_info  # pragma: no cover
from backend.src.utils.SQLutils.user_send import cast_workouts_to_trios, send_user_all, send_user_creds  # pragma: no cover
from backend.src.utils.user_storage.user import user  # pragma: no cover
from backend.src.utils.SQLutils.config import DB_CREDENTIALS  # pragma: no cover
from psycopg2.extras import register_composite  # pragma: no cover


test_user = user(dob="2005-03-17", sex="Male", running_ex="Advanced", injury=0, most_recent_injury=0,
                 longest_run=12, goal_date="2026-01-01", available_days=[1, 1, 0, 1, 1, 2, 1], number_of_days=7,
                 pace_estimates=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
database = txt_to_database("backend/data/raw/training_plan_test.txt")
test_user.day_future = database.day
test_user.week_future = database.week
test_user.month_future = database.month


def test_user_cycle():
    assert send_user_all(
        test_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
    retrieved_user = populate_user_info(test_user.user_id)
    print(test_user.user_id)
    database = txt_to_database("backend/data/raw/training_plan_test.txt")

    # Check if the retrieved user matches the test user
    assert retrieved_user == test_user, "Retrieved user does not match the test user"

    # test the month queue
    for i in range(len(retrieved_user.month_future.queue)):
        assert retrieved_user.month_future.queue[i] == database.month.queue[
            i], f"Month queue mismatch at index {i}"
    # test the week queue
    assert retrieved_user.week_future.queue == database.week.queue
    # test the day queue
    assert retrieved_user.day_future.queue == database.day.queue


def test_SQL_trio_to_tuple():
    day = database.day.get()
    day.workouts = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]

    conn = init_db(DB_CREDENTIALS["DB_USERNAME"],
                   DB_CREDENTIALS["DB_PASSWORD"])
    cursor = conn.cursor()

    TrioType = register_composite(
        'trio', conn, globally=True).type  # No errors = good

    raw_workouts = [(1.0, 2.0, 3.0), (4.0, 5.5, 6.0), (7.0, 8.0, 9.0)]
    # # Minimal, valid trio array
    casted_workouts = cast_workouts_to_trios(raw_workouts, TrioType)

    user_id = secrets.randbelow(10000000)

    cursor.execute(
        "INSERT INTO day_cycle (user_id, workouts) VALUES (%s, %s::trio[])",
        (user_id, casted_workouts)
    )
    print(user_id)

    cursor.execute(
        "SELECT workouts FROM day_cycle WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    return_workouts = result[0] if result else []
    conn.commit()
    cursor.close()
    conn.close()

    assert raw_workouts == convert_trio_types_to_tuples(return_workouts)


def test_user_credentials():
    """
    Test the user credentials functionality.
    """
    test_user_id = secrets.randbelow(10000000)

    login_info = {
        "username": "test_user",
        "password": "test_password",
        "email": "test_user@example.com"
    }

    # Send user credentials to the database
    send_user_creds(
        test_user_id, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"], login_info)

    # Retrieve user credentials from the database
    query = """SELECT username, password, email FROM public.user_credentials WHERE user_id = %s;"""

    conn = init_db(DB_CREDENTIALS["DB_USERNAME"],
                   DB_CREDENTIALS["DB_PASSWORD"])
    cursor = conn.cursor()
    cursor.execute(query, (test_user_id,))

    result = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    assert result[0] == login_info["username"], "Username does not match the expected value"
    assert result[1] == login_info["password"], "Password does not match the expected value"
    assert result[2] == login_info["email"], "Email does not match the expected value"
