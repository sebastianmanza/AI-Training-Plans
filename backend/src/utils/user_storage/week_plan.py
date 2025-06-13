import backend.src.utils.user_storage.day_plan as day_plan


class week_plan:
    __slots__ = ("total_mileage", "completed_mileage", "percent_completion",
                 "goal_stimuli", "cycle", "days", "expected_rpe", "real_rpe")

    global DAYS_IN_WEEK
    DAYS_IN_WEEK = 7

    def __init__(self, total_mileage: int, goal_stimuli: str, cycle: str, expected_rpe):
        self.total_mileage = total_mileage
        self.completed_mileage = 0
        self.percent_completion = 0

        self.goal_stimuli = goal_stimuli
        self.cycle = cycle

        self.days = []
        self.expected_rpe = expected_rpe
        self.real_rpe = 0

    # Once we have the days add them to the week
    def add_days(self, *days):
        for day in days:
            self.days.append(day)

    def update_weekly_real_rpe(self):
        """
        Update the real RPE for the week based on the expected and real RPE values.
        """
        total = 0  # Total the RPE
        for day in self.days:
            total += day.real_rpe
        self.real_rpe = total / DAYS_IN_WEEK

    def update_weekly_mileage(self):
        """
        Update the weekly completion based on the daily completion.
        """
        total = 0  # Total the completion scores
        for day in self.days:
            total += day.completed_mileage  # Sum the completed mileage for each day
        self.completed_mileage = total
        self.update_weekly_percent()

    def update_weekly_percent(self):
        """
        Update the weekly completion percentage based on the total mileage and completed mileage.
        """
        self.percent_completion = self.completed_mileage / \
            self.total_mileage if self.total_mileage > 0 else 1

    # Note that updating mileage also updates the percentage
    def update_week(self):
        """
        Update the weekly mileage and RPE.
        """
        self.update_weekly_mileage()
        self.update_weekly_real_rpe()
