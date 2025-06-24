from backend.src.utils.user_storage.user import user
from backend.src.utils.user_storage.training_database import training_database
from backend.src.utils.SQLutils.user_send import send_user_info
from backend.src.utils.SQLutils.user_retrieve import populate_user_info


test_user = user(20, "male", "advanced", "17:45", "3/14/2026", 5, 2)
test_user.day_future = training_database.day
test_user.week_future = training_database.week
test_user.month_future = training_database.month

def test_user_cycle():
    """
    Test the user cycle functionality.
    """
    send_user_info(test_user)
    
    return_user = populate_user_info(test_user.user_id)
    
   