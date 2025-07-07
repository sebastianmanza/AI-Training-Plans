from backend.src.utils.workout.workout_storage import workout_storage
from backend.src.utils.workout.single_workout import single_workout
from math import sqrt

TRIO_STIM, TRIO_RPE, TRIO_DIST = 0, 1, 2
LARGE_NUM = 4000


class workout_database:

    storage = workout_storage()

    # Creates a trio that can be used as a key in the workout dictionary.
    @staticmethod
    def create_trio(stim, rpe, dist):
        stim, rpe, dist = float(stim), float(rpe), float(dist)
        return (stim, rpe, dist)

    # x range is 1 - 7 stimulus, y range is 1 -10 RPE, z range is 1 - 10 Distance
    # Dictionary that maps trios of (x, y, z) coordinates to workout types.
    workout_dictionary = {
        create_trio(2.5, 4, 5.5): "ET",
        create_trio(2, 3, 4.5): "Recovery",
        create_trio(4, 6, 6): "Kenyan",
        create_trio(2.5, 5, 10): "Long",
        create_trio(4.5, 7, 7.5): "Threshold",
        create_trio(5, 6, 7): "Fartlek",
        create_trio(5.5, 8, 6.5): "Race Pace Interval",
        create_trio(6.5, 2, .5): "Strides",
        create_trio(7, 3, .5): "Hill Sprints",
        create_trio(7, 6, .5): "Flat Sprints",
        create_trio(6, 10, 3): "Time Trial",
        create_trio(1, 2, 3): "Warmup and Cooldown",
        create_trio(0, 0, 0,): "Off"
    }

    def __init__(self, et=list, recovery=list, kenyan=list,
                 long=list, threshold=list, fartlek=list,
                 race_pace_interval=list, strides=list, hill_sprints=list,
                 flat_sprints=list, time_trial=list, warmup_and_cooldown=list):

        # Set up the collection of workouts of each type
        self.et = workout_database.storage.et
        self.recovery = workout_database.storage.recovery
        self.kenyan = workout_database.storage.kenyan
        self.long = workout_database.storage.long
        self.threshold = workout_database.storage.threshold
        self.fartlek = workout_database.storage.fartlek
        self.race_pace_interval = workout_database.storage
        self.strides = workout_database.storage.strides
        self.hill_sprints = workout_database.storage.hill_sprints
        self.flat_sprints = workout_database.storage.flat_sprints
        self.time_trial = workout_database.storage.time_trial
        self.warmup_and_cooldown = workout_database.storage.warmup_and_cooldown

    def add_workout(self, workout: single_workout) -> None:
        """Add a workout to the matching workout database"""
        workout_type = workout_database.get_workout_type(
            workout.trio[TRIO_STIM], workout.trio[TRIO_RPE], workout.trio[TRIO_DIST])
        if workout_type == "ET":
            workout_database.storage.et.append(workout)
        elif workout_type == "Recovery":
            workout_database.storage.recovery.append(workout)
        elif workout_type == "Kenyan":
            workout_database.storage.kenyan.append(workout)
        elif workout_type == "Long":
            workout_database.storage.long.append(workout)
        elif workout_type == "Threshold":
            workout_database.storage.threshold.append(workout)
        elif workout_type == "Fartlek":
            workout_database.storage.fartlek.append(workout)
        elif workout_type == "Race Pace Interval":
            workout_database.storage.race_pace_interval.append(workout)
        elif workout_type == "Strides":
            workout_database.storage.strides.append(workout)
        elif workout_type == "Hill Sprints":
            workout_database.storage.hill_sprints.append(workout)
        elif workout_type == "Flat Sprints":
            workout_database.storage.flat_sprints.append(workout)
        elif workout_type == "Time Trial":
            workout_database.storage.time_trial.append(workout)
        else:
            workout_database.storage.warmup_and_cooldown.append(workout)

    def mass_add_workouts(self, workouts) -> None:
        """"Add a list of workouts to the database"""
        for workout in workouts:
            if not (isinstance(workout, single_workout)):
                raise (
                    "Tried to add something that isn't a workout to the workout database")
            else:
                self.add_workout(workout)

    def print_workouts(self, workout_type: str) -> None:
        """Print out every workout of an inputted type"""
        if workout_type == "ET":
            print("ET Workouts:")
            for workout in self.et:
                print(workout)
        elif workout_type == "Recovery":
            print("Recovery Workouts:")
            for workout in self.recovery:
                print(workout)
        elif workout_type == "Kenyan":
            print("Kenyan Workouts:")
            for workout in self.kenyan:
                print(workout)
        elif workout_type == "Long":
            print("Long Workouts:")
            for workout in self.long:
                print(workout)
        elif workout_type == "Threshold":
            print("Threshold Workouts:")
            for workout in self.threshold:
                print(workout)
        elif workout_type == "Fartlek":
            print("Fartlek Workouts:")
            for workout in self.fartlek:
                print(workout)
        elif workout_type == "Race Pace Interval":
            print("Race Pace Interval Workouts:")
            for workout in self.race_pace_interval:
                print(workout)
        elif workout_type == "Strides":
            print("Strides Workouts:")
            for workout in self.strides:
                print(workout)
        elif workout_type == "Hill Sprints":
            print("Hill Sprints Workouts:")
            for workout in self.hill_sprints:
                print(workout)
        elif workout_type == "Flat Sprints":
            print("Flat Sprints Workouts:")
            for workout in self.flat_sprints:
                print(workout)
        elif workout_type == "Time Trial":
            print("Time Trial Workouts:")
            for workout in self.time_trial:
                print(workout)
        else:
            workout_type == "Warmup and Cooldown"
            print("Warmup and Cooldown Workouts:")
            for workout in self.warmup_and_cooldown:
                print(workout)

    # Returns a workout type based on the given x,y and z coordinates represented as stim, rpe and dist.
    @staticmethod
    def get_workout_type(stim: float, rpe: float, dist: float):
        """Returns the workout type based on stim, rpe, and dist"""
        distance = LARGE_NUM
        final_trio = workout_database.create_trio(0, 0, 0)
        for trio in workout_database.workout_dictionary:
            new_distance = workout_database.get_distance(trio, stim, rpe, dist)
            if new_distance < distance:
                distance = new_distance
                final_trio = trio

        # If the distance isn't 0 then a workout type hasn't been found.
        if final_trio == (0, 0, 0) and not dist == 0:
            raise ValueError(
                "No matching workout type found for the given coordinates.")

        return workout_database.workout_dictionary[final_trio]

    def get_workout_storage_type(self, workout_type: str) -> list:
        if workout_type == "ET":
            return workout_database.storage.et
        elif workout_type == "Recovery":
            return workout_database.storage.recovery
        elif workout_type == "Kenyan":
            return workout_database.storage.kenyan
        elif workout_type == "Long":
            return workout_database.storage.long
        elif workout_type == "Threshold":
            return workout_database.storage.threshold
        elif workout_type == "Fartlek":
            return workout_database.storage.fartlek
        elif workout_type == "Race Pace Interval":
            return workout_database.storage
        elif workout_type == "Strides":
            return workout_database.storage.strides
        elif workout_type == "Hill Sprints":
            return workout_database.storage.hill_sprints
        elif workout_type == "Flat Sprints":
            return workout_database.storage.flat_sprints
        elif workout_type == "Time Trial":
            return workout_database.storage.time_trial
        else:
            return workout_database.storage.warmup_and_cooldown

    def get_individual_workout_helper(self, stim: float, rpe: float, dist: float, workout_type: str) -> single_workout:
        """Returns the workout closest to the stim,rpe and dist from within the type"""
        distance = LARGE_NUM  # A value large enough to not be the min
        final_workout = workout_database.storage.workout_type[0]
        for workout in workout_database.storage.workout_type:
            new_distance = workout_database.get_distance(
                workout.get_trio(), stim, dist, rpe)
            if new_distance < distance:
                distance = new_distance
                final_workout = workout

        return final_workout

    def get_individual_workout(self, stim: float, rpe: float, dist: float) -> single_workout:
        workout_type = workout_database.get_workout_type(
            stim, rpe, dist)  # Get the workout type based on the trio
        # Find the closest workout within the particular database
        workout_type = workout_database.get_workout_storage_type(
            self, workout_database.get_workout_type(stim, rpe, dist))
        return workout_database.get_individual_workout_helper(self, stim, rpe, dist, workout_type)

    def get_workout_type_coordinates(stim: float, rpe: float, dist: float):
        """Given stim, rpe, and dist return the coordinates associated with the workout type"""
        distance = LARGE_NUM
        final_trio = workout_database.create_trio(0, 0, 0)
        for trio in workout_database.workout_dictionary:
            new_distance = workout_database.get_distance(trio, stim, rpe, dist)
            if new_distance < distance:
                distance = new_distance
                final_trio = trio

        if final_trio == (0, 0, 0) and not dist == 0:
            raise ValueError(
                "No matching workout type found for the given coordinates.")

        return final_trio

    def get_workout_difference(stim: float, rpe: float, dist: float):
        """Return the difference between the inputted stim, rpe, and dist and the workout type it is associated with"""
        workout_trio = workout_database.get_workout_type_coordinates(
            stim, rpe, dist)
        return workout_database.create_trio(
            (stim - workout_trio[TRIO_STIM]),
            (rpe - workout_trio[TRIO_RPE]),
            (dist - workout_trio[TRIO_DIST]))

    def get_distance(trio, stim: float, rpe: float, dist: float) -> float:
        return (trio[TRIO_STIM] - stim) ** 2 + (trio[TRIO_RPE] - rpe) ** 2 + (trio[TRIO_DIST] - dist) ** 2
