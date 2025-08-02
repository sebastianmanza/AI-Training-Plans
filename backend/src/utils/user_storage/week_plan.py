import backend.src.utils.user_storage.day_plan as day_plan
import backend.src.utils.user_storage.month_plan as month_plan
from backend.src.utils.workout.workout_database import workout_database
from backend.src.utils.pace_calculations import average_property


DAYS_IN_WEEK = 7  # Default number of days in a week


class week_plan:
    __slots__ = ("total_mileage", "completed_mileage", "percent_completion",
                 "goal_stimuli", "cycle", "days", "expected_rpe", "real_rpe", "month_id", "week_id")

    def __init__(self, total_mileage: int = -1, goal_stimuli=workout_database.create_trio(-1, -1, -1), cycle: str = "", expected_rpe=-1, month_id: int = -1, real_rpe: int = 0, completed_mileage: int = 0, percent_completion: int = 0, days: list | None = None, week_id: int = -1):
        """Creates a week plan object autofilled with placeholders

        Args:
            total_mileage (int, optional): The total mileage of the week. Defaults to -1.
            goal_stimuli (trio, optional): The goal stimuli trio of the week. Defaults to workout_database.create_trio(-1, -1, -1).
            cycle (str, optional): The cycle of the week (Build, hold, etc). Defaults to "".
            expected_rpe (int, optional): The expected RPE of the week. Defaults to -1.
            month_id (int, optional): The ID of the week. Defaults to -1.
            real_rpe (int, optional): The RPE of the week. Defaults to 0.
            completed_mileage (int, optional): The total finished mileage of the week. Defaults to 0.
            percent_completion (int, optional): A completion score. Defaults to 0.
            days (list, optional): A list of the days contained in the week. Defaults to [].
            week_id (int, optional): The ID of the week (unique). Defaults to -1.
        """
        self.week_id = week_id
        self.total_mileage = total_mileage
        self.completed_mileage = completed_mileage
        self.percent_completion = percent_completion

        self.goal_stimuli = goal_stimuli
        self.cycle = cycle

        self.days = days if days is not None else []
        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe

        self.month_id = month_id  # Reference to the month plan this week belongs to

    def add_days(self, days) -> None:
        """ Add multiple days to the week plan."""
        for day in days:
            self.days.append(day)

    # Update methods which includes the ability to set values
    def update_weekly_real_rpe(self) -> None:
        """Update the real RPE for the week based on the expected and real RPE values."""
        self.real_rpe = average_property(self.days, 'real_rpe')

    def update_weekly_mileage(self) -> None:
        """Update the weekly completion based on the daily completion."""
        self.completed_mileage = average_property(
            self.days, 'completed_mileage')
        self.update_weekly_percent()

    def update_weekly_percent(self) -> None:
        """Update the weekly completion percentage based on the total mileage and completed mileage."""
        self.percent_completion = self.completed_mileage / \
            self.total_mileage if self.total_mileage > 0 else 1

    # Note that updating mileage also updates the percentage
    def update_week(self) -> None:
        """Update the weekly mileage and RPE."""
        self.update_weekly_mileage()
        self.update_weekly_real_rpe()
        self.month_id.update_monthly_mileage()

    def __eq__(self, other) -> bool:
        """Check if two week_plan objects are equal based on their attributes."""
        if not isinstance(other, week_plan):
            return False

        return (self.total_mileage == other.total_mileage and
                self.goal_stimuli == other.goal_stimuli and
                self.cycle == other.cycle and
                self.expected_rpe == other.expected_rpe and
                self.month_id == other.month_id and
                self.real_rpe == other.real_rpe and
                self.completed_mileage == other.completed_mileage and
                self.percent_completion == other.percent_completion and
                self.week_id == other.week_id and
                self.goal_stimuli == other.goal_stimuli and
                len(self.days) == len(other.days) and
                all(day1 == day2 for day1, day2 in zip(self.days, other.days))
                )

    def __repr__(self) -> str:
        """Return debug representation of the week plan."""
        return (
            f"week_plan("
            f"week_id={self.week_id!r}, "
            f"total_mileage={self.total_mileage!r}, "
            f"goal_stimuli={self.goal_stimuli!r}, "
            f"cycle={self.cycle!r}, "
            f"days={self.days!r}, "
            f"percent_completion={self.percent_completion!r}, "
            f"completed_mileage={self.completed_mileage!r}, "
            f"expected_rpe={self.expected_rpe!r}, "
            f"real_rpe={self.real_rpe!r}"
            f"month_id={self.month_id!r}, "
            f"dayslength = {len(self.days)}"
            f")"
        )
