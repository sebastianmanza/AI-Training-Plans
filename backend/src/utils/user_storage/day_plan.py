import backend.src.utils.user_storage.week_plan as week_plan
from backend.src.utils.workout.workout_type_library import *


class day_plan:
    __slots__ = ("total_mileage", "completed_mileage", "goal_stimuli",
                 "lift", "expected_rpe", "real_rpe", "percent_completion", "workout")

    def __init__(self, workouts, total_mileage: int, lift: bool, expected_rpe, week_id: week_plan, 
                 real_rpe: int = 0, completed_mileage: int = 0, percent_completion: int = 0):
        
        self.workouts = workouts
        self.total_mileage = total_mileage
        self.completed_mileage = completed_mileage
        self.percent_completion = percent_completion

        if workouts.len() < 1:
            self.goal_stimuli = workouts[0]
        else:
            x = 0
            y = 0
            z = 0
            for trios in workouts:
                if(trios[0]> x and trios[2] > 1):
                    x = trios[0]
                if(trios[1] > y):
                    y = trios[1]
                z = z + trios[z]
            self.goal_stimuli = workout_type_library.create_trio(x, y, z)

        self.lift = lift
        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe
        self.workouts = workouts

        self.week_id = week_id  # Reference to the week plan this day belongs to

    def add_workouts(self, *workouts):
        for workout in workouts:
            self.workouts.append(workout)

    def update__real_rpe(self, real_rpe: int):
        """
        Update the real RPE for the day.

        Args:
            real_rpe (int): The real RPE value for the day.
        """
        self.real_rpe = real_rpe

    def update_daily_mileage(self, mileage: int):
        """
        Update the completed mileage for the day.

        Args:
            mileage (int): The mileage completed for the day.
        """
        self.completed_mileage = mileage
        self.update_daily_percentage()  # Update the completion percentage

    def update_daily_percentage(self):
        """
        Update the completion percentage based on the total and completed mileage.
        """
        self.percent_completion = self.completed_mileage / \
            self.total_mileage if self.total_mileage > 0 else 1

    # Note that updating mileage also updates the percentage
    def update_day(self, mileage: int, real_rpe: int):
        """
        Update the daily mileage and RPE.

        Args:
            mileage (int): The mileage completed for the day.
            real_rpe (int): The real RPE value for the day.
        """
        self.update_daily_mileage(mileage)
        self.update__real_rpe(real_rpe)
        #self.week_id.update_week()
