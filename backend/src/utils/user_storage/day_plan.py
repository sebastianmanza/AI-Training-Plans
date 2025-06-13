class day_plan:
    __slots__ = ("total_mileage", "completed_mileage", "goal_stimuli",
                 "lift", "expected_rpe", "real_rpe", "percent_completion", "workout")

    def __init__(self, total_mileage: int, goal_stimuli: str, lift: bool, expected_rpe):
        self.total_mileage = total_mileage
        self.completed_mileage = 0
        self.percent_completion = 0

        self.goal_stimuli = goal_stimuli
        self.lift = lift

        self.expected_rpe = expected_rpe
        self.real_rpe = 0
        self.workouts = []

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

    def run_updates(self, mileage: int, real_rpe: int):
        """
        Update the daily mileage and RPE.

        Args:
            mileage (int): The mileage completed for the day.
            real_rpe (int): The real RPE value for the day.
        """
        self.update_daily_mileage(mileage)
        self.update__real_rpe(real_rpe)
