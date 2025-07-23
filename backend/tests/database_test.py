from backend.scripts.txt_to_database import txt_to_database
from backend.src.utils.SQLutils.user_retrieve import populate_user_info
from backend.src.utils.SQLutils.user_send import send_user_all
from backend.src.utils.user_storage.user import user
from backend.src.utils.SQLutils.config import DB_CREDENTIALS


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
    
    
    
    