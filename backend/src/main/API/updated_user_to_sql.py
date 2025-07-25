import json
from backend.src.utils.SQLutils import user_send, user_retrieve
from backend.src.utils.workout.workout_database import workout_database
from backend.src.utils.RPEutils import completion_score
from backend.src.utils.user_storage.user import update_mean_RPE
from backend.src.utils.SQLutils.config import DB_CREDENTIALS

class UpdatedUserToSQL:
    @staticmethod
    def update_user(payload: dict) -> dict:
        """
        Updates user information in the database based on the provided payload.
        """
        user_id = payload["user_id"]
        # Retrieve current user from DB
        current_user = user_retrieve.populate_user_info(user_id)
        current_day = current_user.day_future.get()
        primary_workout = None
        for workout in current_day.workouts:
            if primary_workout is None or workout.get_rpe() > primary_workout.get_rpe():
                primary_workout = workout

        wd = workout_database()
        workout_type = wd.get_workout_type(primary_workout.get_stim(),
                                           primary_workout.get_rpe(),
                                           primary_workout.get_distance())


        # Update user fields from payload
        # Example: update RPE, mileage, etc.
        if "workout_RPE" in payload:
            current_user.update_mean_RPE(payload["workout_RPE"], current_user.workout_RPE[0])
        if "mileage" in payload:
            current_day.completed_mileage = payload["mileage"]
        # Add more fields as needed...
        if "reps" or "pace" in payload:
            if "reps" in payload:
                observed_reps = payload["reps"]
            else:
                observed_reps = primary_workout.get_reps()
            if "pace" in payload:
                observed_pace = payload["pace"]
            else:
                observed_pace = primary_workout.get_pace()
        current_day.percent_completion = completion_score(expected_reps=primary_workout.get_reps(),
                                                          observed_reps=observed_reps,
                                                          expected_pace=primary_workout.get_pace(),
                                                          observed_pace=observed_pace)
            
        # Send updated user back to DB
        current_user.day_history.append(current_day)
        user_send.send_user_all(current_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])

        return {"status": "success", "user_id": user_id}
    