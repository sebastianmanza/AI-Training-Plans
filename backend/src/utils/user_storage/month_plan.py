import backend.src.utils.user_storage.week_plan as week_plan


class month_plan:
    __slots__ = ("total_mileage", "goal_stimuli", "cycle", "weeks",
                 "percent_completion", "completed_mileage", "expected_rpe", "real_rpe")

    def __init__(self, total_mileage: int, goal_stimuli: str, cycle: str, expected_rpe):
        self.total_mileage = total_mileage
        self.completed_mileage = 0
        self.percent_completion = 0

        self.goal_stimuli = goal_stimuli
        self.cycle = cycle

        self.weeks = []
        self.expected_rpe = expected_rpe
        self.real_rpe = 0

    # Once we have the weeks add them to the month
    def add_weeks(self, *weeks):
        for week in weeks:
            self.weeks.append(week)

    def update_monthly_real_rpe(self):
        """
        Update the real RPE for the month based on the expected and real RPE values.
        """
        total = 0  # Total the RPE
        for week in self.weeks:
            total += week.calc_weekly_real_rpe()
        # Divide by the number of weeks
        self.real_rpe = total / len(self.weeks) if self.weeks else 0

    def update_monthly_mileage(self):
        """
        Update the monthly completion based on the weekly completion.
        """
        total = 0  # Total the weekly mileage
        for week in self.weeks:
            total += week.completed_mileage  # Sum the completed mileage for each week
        self.completed_mileage = total
        self.update_monthly_percent()

    def update_monthly_percent(self):
        """
        Update the monthly completion percentage based on the total and completed mileage.
        """
        self.percent_completion = self.completed_mileage / \
            self.total_mileage if self.total_mileage > 0 else 1

    # Note that updating mileage also updates the percentage
    def update_week(self):
        """
        Update the monthly mileage and RPE.
        """
        self.update_monthly_mileage()
        self.update_monthly_real_rpe()
