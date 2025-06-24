import sys
import os

# Dynamically find the root directory containing the 'backend' folder
current_dir = os.path.dirname(__file__)
while not os.path.exists(os.path.join(current_dir, "backend")):
    current_dir = os.path.dirname(current_dir)
    if current_dir == "/":  # Stop if we reach the root of the filesystem
        raise RuntimeError("Could not find 'backend' folder in the directory hierarchy.")

# Add the root directory to the Python path
sys.path.append(current_dir)


from backend.src.utils.user_storage.user import user
from backend.src.utils.user_storage.training_database import training_database
from backend.src.utils.SQLutils.user_send import send_user_all
from backend.src.utils.SQLutils.user_retrieve import populate_user_info
from backend.src.main.survey import main
from backend.src.utils.SQLutils.config import DB_CREDENTIALS


test_user = user(12345, "male", "advanced", "17:45", 4, 5, 2)
test_user.day_future = training_database.day
test_user.week_future = training_database.week
test_user.month_future = training_database.month


def test_user_cycle():
    """
    Test the user cycle functionality.
    """
    
    #test_user = main.prelim_survey()
    send_user_all(test_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
    
    return_user = populate_user_info(test_user.user_id)
    
    print("working")
    # return 
    print(test_user.user_id)
    print(return_user.user_id)
    print(return_user.age)
    print(return_user.sex)
    

test_user_cycle()
    
    