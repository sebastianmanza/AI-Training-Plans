import backend.src.utils.user_storage.week_plan as week_plan
from backend.src.utils.workout.workout_type_library import *


class day_plan:
    __slots__ = ("total_mileage", "completed_mileage", "goal_stimuli",
                 "lift", "expected_rpe", "real_rpe", "percent_completion", "workouts", "week_id")

    def __init__(self, workouts: list = [], total_mileage: int = -1, lift: bool = False, expected_rpe = -1, week_id: int = -1, 
                 real_rpe: int = 0, completed_mileage: int = 0, percent_completion: int = 0):
        
        self.workouts = workouts
        self.total_mileage = total_mileage
        self.completed_mileage = completed_mileage
        self.percent_completion = percent_completion

        if len(workouts) < 1:
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
                z = z + trios[2]
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

day = day_plan([(1, 3, 4), (4, 5, 6)], 10, False, 6, 1, 9, 10, 1)
print("stim 1")
print(day.workouts[0])
print("stim 2")
print(day.workouts[1])
print("goal stimuli")
print(day.goal_stimuli)
'''day_two = day_plan([(1, 3, 4)], 10, False, 6, 1, 9, 10, 1)
print("stim 1")
print(day_two.workouts[0])
print("goal stimuli")
print(day_two.goal_stimuli)'''