import secrets
from backend.src.utils.user_storage import day_plan
from backend.src.utils.user_storage import user, week_plan
from backend.src.utils.user_storage.month_plan import month_plan
from backend.src.utils.SQLutils import user_send
from backend.src.utils.user_storage.storage_stacks_and_queues import *
import psycopg2
import datetime


class main:

    def prelim_survey(payload: dict) -> dict:
        """
        payload is a dictionary of original questions and answers
        """

        new_user = user.user(
            payload["date_of_birth"],
            payload["sex"],
            payload["running_experience"],
            payload["days_per_week"],
            payload["days_of_week"],
            payload["most_time_day"],
            payload["current_5k_fitness"],
            payload["major_injuries"],
            payload["most_recent_injury"],
        )
        # send it to your DB
        
        #user_send.send_user_info(new_user, "postgres", "Control1500#")

        # return a simple acknowledgement
        return {
            "status": "ok",
            }
    # testing 
    # user_send.send_user_info(prelim_survey(), "postgres", "Control1500#")
      
