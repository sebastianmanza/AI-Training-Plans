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
available_days = ["Mon", "Fri", "Sat"]
list_of_workouts = [1.1, 2.2, 3.3]
login_info = ["conballs@gmail.com", "concon", "secure_password"]

test_user = user("Aug", "M", "Advanced", 1, 2, 12, "Nov", my_dict, available_days, 7, 100, list_of_workouts)
test_user.day_future = database.day
test_user.week_future = database.week
test_user.month_future = database.month


def test_user_cycle():
    """
    Test the user cycle functionality.
    """
# test_user = main.prelim_survey()
    send_user_all(test_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"], login_info)

    return_user = populate_user_info(test_user.user_id)
# #     print("User information retrieved")

# #     # print(database.day.get().expected_rpe)
# #     # print("Day future expected RPE")
# #     # print(test_user.day_future.get().expected_rpe)
# #     # print("working")
# #     # return
    print(test_user.user_id)
    print(return_user.user_id)
    
    print(return_user.sex)