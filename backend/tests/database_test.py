import secrets
from backend.scripts.txt_to_database import txt_to_database
from backend.src.utils.SQLutils.database_connect import init_db, db_select
from backend.src.utils.SQLutils.user_retrieve import convert_trio_types_to_tuples, populate_user_info
from backend.src.utils.SQLutils.user_send import cast_workouts_to_trios, send_user_all, send_user_creds
from backend.src.utils.user_storage.user import user
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from psycopg2.extras import register_composite


test_user = user(dob = "2005-03-17", sex = "Male", running_ex="Advanced", injury = 0, most_recent_injury = 0,
                 longest_run=12, goal_date="2026-01-01", available_days=[1, 1, 0, 1, 1, 2, 1], number_of_days=7, 
                 pace_estimates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
database = txt_to_database("backend/data/raw/training_plan_test.txt")
test_user.day_future = database.day
test_user.week_future = database.week
test_user.month_future = database.month

def test_user_cycle(): 
    send_user_all(test_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
    retrieved_user = populate_user_info(test_user.user_id)
    print(test_user.user_id)
    database = txt_to_database("backend/data/raw/training_plan_test.txt")
    
    # Check if the retrieved user matches the test user
    assert retrieved_user == test_user, "Retrieved user does not match the test user"
    
    # test the month queue
    for i in range(len(retrieved_user.month_future.queue)):
        assert retrieved_user.month_future.queue[i] == database.month.queue[i], f"Month queue mismatch at index {i}"
    # test the week queue
    assert retrieved_user.week_future.queue == database.week.queue
    # test the day queue
    assert retrieved_user.day_future.queue == database.day.queue
    
def test_SQL_trio_to_tuple():
    day = database.day.get() 
    day.workouts = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    
    conn = init_db(DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
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
    
    cursor.execute("SELECT workouts FROM day_cycle WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    return_workouts = result[0] if result else []
    conn.commit()
    cursor.close()
    conn.close()
    
    assert raw_workouts == convert_trio_types_to_tuples(return_workouts)
    

# def test_user_credentials():
#     """
#     Test the user credentials functionality.
#     """
#     test_user_id = secrets.randbelow(10000000)
    
#     login_info = {
#         "username": "test_user",
#         "password": "test_password",
#         "email": "test_user@example.com"
#     }
    
#     # Send user credentials to the database
#     send_user_creds(test_user_id, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"], login_info)
    
#     # Retrieve user credentials from the database
#     query = """SELECT username, password, email FROM public.user_credentials WHERE user_id = %s;"""
    
#     conn = init_db(DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
#     cursor = conn.cursor()
#     cursor.execute(query, (test_user_id,))
    
#     result = cursor.fetchall()
    
#     conn.commit()
#     cursor.close()
#     conn.close()
    
#     assert result == [login_info["username"], login_info["password"], login_info["email"]], "User credentials do not match the expected values"
    
    
    
    
    

     