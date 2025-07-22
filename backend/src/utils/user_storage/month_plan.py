import backend.src.utils.user_storage.week_plan as week_plan
from backend.src.utils.workout.workout_database import workout_database
from backend.src.utils.pace_calculations import average_property


class month_plan:
    __slots__ = ("month_id", "total_mileage", "goal_stimuli", "cycle", "weeks",
                 "percent_completion", "completed_mileage", "expected_rpe", "real_rpe")

    def __init__(self, month_id: int = -1, total_mileage: int = 0, goal_stimuli=workout_database.create_trio(0, 0, 0), cycle: str = "", expected_rpe: int = 0, real_rpe: int = 0, completed_mileage: int = 0, percent_completion: int = 0, weeks: list = []):
        """_summary_

        Args:
            month_id (int, optional): _description_. Defaults to -1.
            total_mileage (int, optional): _description_. Defaults to 0.
            goal_stimuli (_type_, optional): _description_. Defaults to workout_database.create_trio(0, 0, 0).
            cycle (str, optional): _description_. Defaults to "".
            expected_rpe (int, optional): _description_. Defaults to 0.
            real_rpe (int, optional): _description_. Defaults to 0.
            completed_mileage (int, optional): _description_. Defaults to 0.
            percent_completion (int, optional): _description_. Defaults to 0.
            weeks (list, optional): _description_. Defaults to [].

        Raises:
            TypeError: _description_
        """
        self.weeks = weeks
        for week in self.weeks:  # Ensure that each week is of type week_plan
            if not isinstance(week, week_plan.week_plan):
                raise TypeError(
                    "All weeks must be instances of week_plan.week_plan")
        self.month_id = month_id
        self.total_mileage = total_mileage
        self.completed_mileage = completed_mileage
        self.percent_completion = percent_completion

        self.goal_stimuli = goal_stimuli
        self.cycle = cycle

        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe

    # Once we have the weeks add them to the month. May be removed
    def add_weeks(self, weeks) -> None:
        """ Add multiple weeks to the month plan."""
        for week in weeks:
            if not isinstance(week, week_plan.week_plan):
                raise TypeError(
                    "All weeks must be instances of week_plan.week_plan")
            self.weeks.append(week)

    def update_monthly_real_rpe(self) -> None:  # FIXED: Removed unexpected indentation
        """Update the real RPE for the month based on the expected and real RPE values."""
        self.real_rpe = average_property(self.weeks, 'real_rpe')

        def update_monthly_mileage(self) -> None:
            """Update the monthly completion based on the weekly completion."""
            self.completed_mileage = average_property(
                self.weeks, 'completed_mileage')
            # Update the percentage after updating completed mileage
            self.update_monthly_percent()

    def update_monthly_percent(self) -> None:
        """Update the monthly completion percentage based on the total and completed mileage."""
        self.percent_completion = self.completed_mileage / \
            self.total_mileage if self.total_mileage > 0 else 1

    # Note that updating mileage also updates the percentage
    def update_week(self) -> None:
        """Update the monthly mileage and RPE."""
        self.update_monthly_mileage()
        self.update_monthly_real_rpe()
        
    def __eq__(self, other) -> bool:
        """Check if two month_plan objects are equal based on their attributes."""
        if not isinstance(other, month_plan):
            return False
        
        return (self.total_mileage == other.total_mileage and
                # self.goal_stimuli == other.goal_stimuli and
                self.cycle == other.cycle and
                self.expected_rpe == other.expected_rpe and
                self.month_id == other.month_id and
                self.real_rpe == other.real_rpe and
                self.completed_mileage == other.completed_mileage and
                self.percent_completion == other.percent_completion)
        
    def __repr__(self) -> str:
        return (
            f"month_plan("
            f"month_id={self.month_id!r}, "
            f"total_mileage={self.total_mileage!r}, "
            f"goal_stimuli={self.goal_stimuli!r}, "
            f"cycle={self.cycle!r}, "
            f"weeks={self.weeks!r}, "
            f"percent_completion={self.percent_completion!r}, "
            f"completed_mileage={self.completed_mileage!r}, "
            f"expected_rpe={self.expected_rpe!r}, "
            f"real_rpe={self.real_rpe!r}"
            f")"
        )
