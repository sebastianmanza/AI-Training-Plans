from backend.src.utils.SQLutils import user_send
from backend.src.utils.user_storage.storage_stacks_and_queues import *
from backend.src.utils.user_storage.user import user
from backend.scripts.txt_to_database import txt_to_database
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.user_storage.user import THREEK, FIVEK, TENK, RECOVERY, EASY, TEMPO, PROGRESSION, THRESHOLD, LONGRUN, VO2MAX
from backend.src.utils.pace_calculations import get_training_pace_helper
from backend.src.utils.decision_tree import decision_tree

class main:
    
    def convert_days_of_week(available_days: list, most_time_day: str) -> list:
        """
        Converts a list of available days of the week into a list of integers.
        0 for unavailable, 1 for available.
        """
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        converted_days = [
            2 if day == most_time_day else
            1 if day in available_days else 0 for day in days]
        
        return converted_days

    def prelim_survey(payload: dict) -> dict:
        """
        payload is a dictionary of original questions and answers
        """
        print(payload)
        
        # Will need to convert to a list of fitnesses
        predicted_5k = payload["current_5k_fitness"]
        
            
        
        # Need to convert available days
        available_days = main.convert_days_of_week(payload["days_of_week"], payload["most_time_day"])

        new_user = user(
            dob = payload["date_of_birth"],
            sex = payload["sex"],
            running_ex = payload["running_experience"],
            injury = payload["major_injuries"],
            most_recent_injury = payload["most_recent_injury"],
            longest_run= payload["longest_run"],
            goal_date = payload["goal_date"],
            available_days = available_days,  # Placeholder for available days
            number_of_days = payload["days_per_week"],
            user_id= payload["user_id"]     
        )
        new_user.pace_estimates[FIVEK] = round(predicted_5k / 3.1) # Assuming 5k is the only distance for now
            
        new_user.pace_estimates[THREEK] = get_training_pace_helper(5000, new_user.pace_estimates[FIVEK] * 3.1, 1.05) # might need adjustment
        new_user.pace_estimates[TENK] = get_training_pace_helper(5000, new_user.pace_estimates[FIVEK] * 3.1, 0.95) # might need adjustment
        new_user.pace_estimates[RECOVERY] = new_user.get_training_pace(RECOVERY)
        new_user.pace_estimates[EASY] = new_user.get_training_pace(EASY)
        new_user.pace_estimates[TEMPO] = new_user.get_training_pace(TEMPO)
        new_user.pace_estimates[PROGRESSION] = new_user.get_training_pace(PROGRESSION)
        new_user.pace_estimates[THRESHOLD] = new_user.get_training_pace(THRESHOLD)
        new_user.pace_estimates[LONGRUN] = new_user.get_training_pace(LONGRUN)
        new_user.pace_estimates[VO2MAX] = new_user.get_training_pace(VO2MAX)
        
        # Convert available days to a list of integers
        
        
        # Static database at the moment: 
        # TODO: Make this the decision tree
        database = decision_tree.get_decision_tree(new_user)
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

    def post_run_survey(payload: dict) -> dict:
        '''Payload is a dictionary of questions and answers for the post run survey'''
      
