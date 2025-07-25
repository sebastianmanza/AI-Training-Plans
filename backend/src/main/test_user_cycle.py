import sys
import os

# Dynamically find the root directory containing the 'backend' folder
current_dir = os.path.dirname(__file__)
while not os.path.exists(os.path.join(current_dir, "backend")):
    current_dir = os.path.dirname(current_dir)
    if current_dir == "/":  # Stop if we reach the root of the filesystem
        raise RuntimeError(
            "Could not find 'backend' folder in the directory hierarchy.")

# Add the root directory to the Python path
sys.path.append(current_dir)
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.scripts.txt_to_database import txt_to_database
from backend.src.main.survey import main
from backend.src.utils.SQLutils.user_retrieve import populate_user_info
from backend.src.utils.SQLutils.user_send import send_user_all
from backend.src.utils.user_storage.training_database import training_database
from backend.src.utils.user_storage.user import user


database = txt_to_database("backend/data/raw/training_plan_test.txt")
# print(database._instance_)
my_dict = [12, 34, 45]
#available_days = ["Mon", "Fri", "Sat"]
available_days = [1, 0, 0, 0, 1, 2, 0]
list_of_workouts = [1.1, 2.2, 3.3]
login_info = ["conballs@gmail.com", "concon", "secure_password"]
pace_estimate = [1, 2, 3]
'''
test_user = user(
                    dob="Aug", 
                    sex="M", 
                    running_ex="Advanced", 
                    injury=1, 
                    most_recent_injury=2, 
                    longest_run=12, 
                    goal_date="Nov", 
                    available_days=available_days, 
                    number_of_days= 5
                )

test_user.day_future = database.day
test_user.week_future = database.week
test_user.month_future = database.month
'''

def test_user_cycle():
    """
    Test the user cycle functionality.
    """
    # test_user = user(
    #     dob="2004-06-27",
    #     sex="Male",
    #     running_ex="Advanced",  
    #     injury=0,
    #     most_recent_injury=0,
    #     longest_run=12,
    #     goal_date="2026-01-01",
    #     available_days=[1, 1, 0, 1, 1, 2, 1],
    #     number_of_days=7,
    # )
    # database = txt_to_database("backend/data/raw/training_plan_test.txt")
    # test_user.day_future = database.day
    # test_user.week_future = database.week
    # test_user.month_future = database.month
    
    
    
    
    #send_user_all(test_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])

    # print(test_user.user_id)
    return_user = populate_user_info(57121620)
    # print(test_user.day_future.get().workouts)
    # print(return_user.day_future.get().workouts)


# test_user_cycle()