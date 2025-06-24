from backend.src.utils.workout.workout_storage import workout_storage
from math import sqrt


class workout_database:

    storage = workout_storage()

    # Creates a trio that can be used as a key in the workout dictionary.
    @staticmethod
    def create_trio(x, y, z):
        return (x, y, z)

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

    def add_workout(self, workout):
        workout_type = workout_database.get_workout_type(
            workout.trio[0], workout.trio[1], workout.trio[2])
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

    def mass_add_workouts(self, workouts):
        for workout in workouts:
            self.add_workout(workout)

    def print_workouts(self, workout_type):
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

    # Returns a workout type based on the given x and y coordinates.
    @staticmethod
    def get_workout_type(x, y, z):
        distance = 100
        final_trio = workout_database.create_trio(0, 0, 0)
        for trio in workout_database.workout_dictionary:
            new_distance = sqrt((trio[0] - x) ** 2 +
                                (trio[1] - y) ** 2 + (trio[2] - z) ** 2)
            if new_distance < distance:
                distance = new_distance
                final_trio = trio

        if final_trio == (0, 0, 0):
            raise ValueError(
                "No matching workout type found for the given coordinates.")

        return workout_database.workout_dictionary[final_trio]

    def get_individual_workout_helper(self, x, y, z, workout_type):
        distance = 100
        final_workout = workout_database.storage.workout_type[0]
        for workout in workout_database.storage.workout_type:
            new_distance = sqrt(
                (workout[0][0] - x) ** 2 + (workout[0][1] - y) ** 2 + (workout[0][2] - z) ** 2)
            if new_distance < distance:
                distance = new_distance
                final_workout = workout

        return final_workout

    def get_individual_workout(self, x, y, z):
        workout_type = workout_database.get_workout_type(x, y, z)
        return workout_database.get_individual_workout_helper(self, x, y, z, workout_type)

    def get_workout_type_coordinates(x, y, z):
        distance = 100
        final_trio = workout_database.create_trio(0, 0, 0)
        for trio in workout_database.workout_dictionary:
            new_distance = sqrt((trio[0] - x) ** 2 +
                                (trio[1] - y) ** 2 + (trio[2] - z) ** 2)
            if new_distance < distance:
                distance = new_distance
                final_trio = trio

        if final_trio == (0, 0, 0):
            raise ValueError(
                "No matching workout type found for the given coordinates.")

        return final_trio

    def get_workout_difference(x, y, z):
        workout_trio = workout_database.get_workout_type_coordinates(x, y, z)
        stimulus_mod = x - workout_trio[0]
        RPE_mod = y - workout_trio[1]
        distance_mod = z - workout_trio[2]
        real_difference = workout_database.create_trio(
            stimulus_mod, RPE_mod, distance_mod)
        return real_difference
