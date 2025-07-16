import backend.src.utils.user_storage.week_plan as week_plan
from backend.src.utils.workout.workout_database import workout_database

TRIO_STIM, TRIO_RPE, TRIO_DIST = 0, 1, 2  # Constants for indexing the trio


class day_plan:

    __slots__ = ("total_mileage", "completed_mileage", "goal_stimuli",
                 "lift", "expected_rpe", "real_rpe", "percent_completion", "workouts", "week_id", "day_id")

    def __init__(self, workouts: list = [], total_mileage: int = -1, lift: bool = False, expected_rpe=-1, week_id: int = -1,
                 real_rpe: int = 0, completed_mileage: int = 0, percent_completion: int = 0, day_id=-1, goal_stimuli=workout_database.create_trio(-1, -1, -1)):

        self.day_id = day_id  # Unique identifier for the day
        self.lift = lift  # Boolean indicating if the day is a lifting day
        self.week_id = week_id
        self.workouts = workouts
        self.total_mileage = total_mileage
        self.completed_mileage = completed_mileage
        self.percent_completion = percent_completion
        self.goal_stimuli = goal_stimuli

        self.lift = lift
        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe
        self.workouts = workouts

        self.week_id = week_id  # Reference to the week plan this day belongs to

        if len(workouts) < 1:  # If there are no workouts the stimuli is for an off day
            self.goal_stimuli = workouts[0]
            return

        self.goal_stimuli = self.__make_stimuli_trio(
            workouts)  # Use the days workouts to create a day trio

    # May not be used if initialized workouts are final

    @staticmethod
    def __make_stimuli_trio(workouts: list) -> tuple:
        """ Create a trio used to define the week using the trios from workouts"""
        tot_stim, tot_rpe, tot_dist = 0, 0, 0
        for trios in workouts:
            # Only consider the stimuli if the distance > 1 (Ignore warmup/cooldown)
            if (trios[TRIO_STIM] > tot_stim and trios[TRIO_DIST] > 1):
                tot_stim = trios[TRIO_STIM]
            if (trios[TRIO_RPE] > tot_rpe):
                tot_rpe = trios[TRIO_RPE]
            tot_dist += trios[TRIO_DIST]
        # Use the values to create the day trio
        return workout_database.create_trio(tot_stim, tot_rpe, tot_dist)

    def add_workouts(self, *workouts) -> None:
        """ Add multiple workouts to the day plan"""
        for workout in workouts:
            self.workouts.append(workout)

    def update__real_rpe(self, real_rpe: int) -> None:
        """ Update the real RPE for the day"""
        self.real_rpe = real_rpe

    def update_daily_mileage(self, mileage: int) -> None:
        """ Update the completed mileage for the day"""
        self.completed_mileage = mileage
        self.update_daily_percentage()  # Update the completion percentage

    def update_daily_percentage(self) -> None:
        """ Update the completion percentage based on the total and completed mileage"""
        self.percent_completion = self.completed_mileage / \
            self.total_mileage if self.total_mileage > 0 else 1

    # Note that updating mileage also updates the percentage
    def update_day(self, mileage: int, real_rpe: int) -> None:
        """ Update the daily mileage and RPE"""
        self.update_daily_mileage(mileage)
        self.update__real_rpe(real_rpe)

        # self.week_id.update_week()
# testing code
'''day = day_plan([(1, 3, 4), (4, 5, 6)], 10, False, 6, 1, 9, 10, 1)
print("stim 1")
print(day.workouts[0])
print("stim 2")
print(day.workouts[1])
print("goal stimuli")
print(day.goal_stimuli)
day_two = day_plan([(1, 3, 4)], 10, False, 6, 1, 9, 10, 1)
print("stim 1")
print(day_two.workouts[0])
print("goal stimuli")
print(day_two.goal_stimuli)'''
