from backend.src.utils.SQLutils import user_send
from backend.src.utils.user_storage.storage_stacks_and_queues import *
from backend.src.utils.user_storage.user import user
from backend.scripts.txt_to_database import txt_to_database
from backend.src.utils.SQLutils.config import DB_CREDENTIALS


class main:

    def prelim_survey(payload: dict) -> dict:
        """
        payload is a dictionary of original questions and answers
        """
        print(payload)
        
        # Will need to convert to a list of fitnesses
        predicted_5k = payload["current_5k_fitness"]
        
        # Need to convert available days
        avaliable_days = payload["days_of_week"]
        
        
        new_user = user(
            dob = payload["date_of_birth"],
            sex = payload["sex"],
            running_ex = payload["running_experience"],
            injury = payload["major_injuries"],
            most_recent_injury = payload["most_recent_injury"],
            longest_run= payload["longest_run"],
            goal_date = payload["goal_date"],
            available_days = [0, 0, 0, 0, 0, 0, 0],  # Placeholder for available days
            number_of_days = payload["days_per_week"],
            user_id= payload["user_id"]     
        )
        # Static database at the moment: 
        # TODO: Make this the decision tree
        database = txt_to_database("backend/data/raw/training_plan_test.txt")
        new_user.day_future = database.day
        new_user.week_future = database.week
        new_user.month_future = database.month
        
        user_send.send_user_all(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])

        # return a simple acknowledgement
        return {
            "status": "ok",
            }
    # testing 
    # user_send.send_user_info(prelim_survey(), "postgres", "Control1500#")
      
