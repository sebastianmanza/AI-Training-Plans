import backend.src.utils.user_storage.day_plan as day_plan
import backend.src.utils.user_storage.month_plan as month_plan
from backend.src.utils.workout.workout_database import workout_database

DAYS_IN_WEEK = 7  # Default number of days in a week


class week_plan:
    __slots__ = ("total_mileage", "completed_mileage", "percent_completion",
                 "goal_stimuli", "cycle", "days", "expected_rpe", "real_rpe", "month_id", "week_id")

    def __init__(self, total_mileage: int = -1, goal_stimuli=workout_database.create_trio(-1, -1, -1), cycle: str = "", expected_rpe=-1, month_id: int = -1, real_rpe: int = 0, completed_mileage: int = 0, percent_completion: int = 0, days: list = [], week_id=-1):
        self.week_id = week_id
        self.total_mileage = total_mileage
        self.completed_mileage = completed_mileage
        self.percent_completion = percent_completion

        self.goal_stimuli = goal_stimuli
        self.cycle = cycle

        self.days = days
        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe

        self.month_id = month_id  # Reference to the month plan this week belongs to

    # Once we have the days add them to the week
    def add_days(self, days):
        """ Add multiple days to the week plan."""
        for day in days:
            self.days.append(day)

    def update_weekly_real_rpe(self):
        """Update the real RPE for the week based on the expected and real RPE values."""
        total = 0  # Total the RPE
        for day in self.days:
            total += day.real_rpe
        self.real_rpe = total / DAYS_IN_WEEK

    def update_weekly_mileage(self):
        """Update the weekly completion based on the daily completion."""
        total = 0  # Total the completion scores
        for day in self.days:  # Sum the completed mileage for each day
            total += day.completed_mileage
        self.completed_mileage = total
        self.update_weekly_percent()

    def update_weekly_percent(self):
        """Update the weekly completion percentage based on the total mileage and completed mileage."""
        self.percent_completion = self.completed_mileage / \
            self.total_mileage if self.total_mileage > 0 else 1

    # Note that updating mileage also updates the percentage
    def update_week(self):
        """Update the weekly mileage and RPE."""
        self.update_weekly_mileage()
        self.update_weekly_real_rpe()
        self.month_id.update_monthly_mileage()
