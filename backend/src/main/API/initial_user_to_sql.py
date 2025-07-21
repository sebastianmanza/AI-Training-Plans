import json
from backend.src.utils.SQLutils import user_send
from backend.src.utils.SQLutils import user_retrieve
from backend.src.utils.user_storage.storage_stacks_and_queues import *
from backend.src.utils.user_storage.user import user
from backend.scripts.txt_to_database import txt_to_database
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.user_storage.user import THREEK, FIVEK, TENK, RECOVERY, EASY, TEMPO, PROGRESSION, THRESHOLD, LONGRUN, VO2MAX
from backend.src.utils.pace_calculations import get_training_pace_helper
from backend.src.utils.decision_tree import decision_tree
from backend.src.utils.RPEutils import completion_score
from backend.src.utils.workout import workout_database
from backend.src.utils.workout.single_workout import get_pace
from backend.src.utils.user_storage import day_plan

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
        print(payload)

        user_id = payload["user_id"]
        workout_rpe = payload["workout_rpe"]
        completion = payload ["completion"]
        mileage = payload["mileage"]
        reps = payload["reps"]
        pace = payload["pace"]
        

        current_user = user_retrieve.populate_user_info(user_id)
        json_string = current_user.workout_RPE
        data_dict = json.loads(json_string)
        workout_rpe = data_dict
        wd = workout_database()

        current_day = current_user.day_future[0]
        for workout in current_day.workouts:
            workout_type = wd.get_workout_type(workout)
            current_user.workout_RPE.workout_type.append(workout_rpe)
        if(completion == False):
            current_user.current_day.completed_mileage = mileage
            current_user.percent_completion = completion_score(expected_reps=wd.get_individual_workout(current_day.workouts[0]), 
                                                               observed_reps=reps, expected_pace=wd.get_individual_workout(current_day.workouts[0]).get_pace()[0],
                                                               observed_pace= pace)
        user_send.send_user_all(user_id, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
      
    user_test = user(dob="06/27/2004",
                     sex="male",
                     running_ex="advanced",
                     injury=0,
                     most_recent_injury=-1,
                     longest_run=11,
                     goal_date="01/01/2026",
                     available_days=[1, 1, 0, 1, 1, 2, 1],
                     )
    test_day = user_test.day_future.get()
    print(test_day.workout_RPE)
    print(test_day.completion)
    print(test_day.mileage)
    print(test_day.reps)
    print(test_day.pace)
    
