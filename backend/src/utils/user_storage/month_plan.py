import backend.src.utils.user_storage.week_plan as week_plan
from backend.src.utils.workout.workout_database import workout_database
from typing import cast, List


class month_plan:
    __slots__ = ("month_id", "total_mileage", "goal_stimuli", "cycle", "weeks",
                 "percent_completion", "completed_mileage", "expected_rpe", "real_rpe")

    def __init__(self, month_id: int = -1, total_mileage: int = 0, goal_stimuli = workout_database.create_trio(0, 0, 0), cycle: str = "", expected_rpe: int = 0, real_rpe: int = 0, completed_mileage: int = 0, percent_completion: int = 0, weeks: list = []):

        self.month_id = month_id
        self.total_mileage = total_mileage
        self.completed_mileage = completed_mileage
        self.percent_completion = percent_completion

        self.goal_stimuli = goal_stimuli
        self.cycle = cycle

        self.weeks = weeks
        for week in self.weeks:
            # Ensure that each week is of type week_plan
            if not isinstance(week, week_plan.week_plan):
                raise TypeError("All weeks must be instances of week_plan.week_plan")
        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe

    # Once we have the weeks add them to the month. May be removed
    def add_weeks(self, weeks) -> None:
        """ Add multiple weeks to the month plan."""
        for week in weeks:
            self.weeks.append(week)

    def update_monthly_real_rpe(self):
        """
        Update the real RPE for the month based on the expected and real RPE values.
        """
        total = 0  # Total the RPE
        for week in self.weeks:
            total += week.calc_weekly_real_rpe()
        self.real_rpe = total / len(self.weeks) if self.weeks else 0 # Divide by the number of weeks

    def update_monthly_mileage(self):
        """
        Update the monthly completion based on the weekly completion.
        """
        total = 0  # Total the weekly mileage
        for week in self.weeks:
            total += week.completed_mileage  # Sum the completed mileage for each week
        self.completed_mileage = total
        self.update_monthly_percent() # Update the percentage after updating completed mileage

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
