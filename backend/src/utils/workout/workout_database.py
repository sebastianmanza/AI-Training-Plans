from backend.src.utils.workout.workout_storage import *


class workout_database:

    storage = workout_storage()

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
        workout_type = workout_type_library.get_workout_type(
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
