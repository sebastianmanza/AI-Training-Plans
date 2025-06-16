from backend.src.utils.workout.workout_type_library import *

class workout_storage:
    #all the workout types
    ## These lists will store different types of workouts.
    et = []
    recovery = []
    kenyan = []
    long = []
    threshold = []
    fartlek = []
    race_pace_interval = []
    strides = []
    hill_sprints = []
    flat_sprints = []
    time_trial = []


    ## Initialize the workout storage with empty lists for threshold and interval workouts.
    def __init__(self):
        w_s = workout_storage
        self.et = w_s.et
        self.recovery = w_s.recovery
        self.kenyan = w_s.kenyan
        self.long = w_s.long
        self.threshold = w_s.threshold
        self.fartlek = w_s.fartlek
        self.race_pace_interval = w_s.race_pace_interval
        self.strides = w_s.strides
        self.hill_sprints = w_s.hill_sprints
        self.flat_sprints = w_s.flat_sprints
        self.time_trial = w_s.time_trial


    ## Add a workout to the appropriate list based on its type.
    ## Raises ValueError if the workout type is unknown.
    def add_workout(self, workout, workout_type):
        if workout_type == "ET":
            self.et.append(workout)
        elif workout_type == "Recovery":
            self.recovery.append(workout)
        elif workout_type == "Kenyan":
            self.kenyan.append(workout)
        elif workout_type == "Long":
            self.long.append(workout)
        elif workout_type == "Threshold":
            self.threshold.append(workout)
        elif workout_type == "Fartlek":
            self.fartlek.append(workout)
        elif workout_type == "Race Pace Interval":
            self.race_pace_interval.append(workout)
        elif workout_type == "Strides":
            self.strides.append(workout)
        elif workout_type == "Hill Sprints":
            self.hill_sprints.append(workout)
        elif workout_type == "Flat Sprints":
            self.flat_sprints.append(workout)
        elif workout_type == "Time Trial":
            self.time_trial.append(workout)
        else:
            raise ValueError(f"Unknown workout type: {workout_type}")

    ## Getters for the workout lists
    #get et workouts
    def get_et_workouts(self):
        return self.et
    #get recovery workouts
    def get_recovery_workouts(self):
        return self.recovery
    #get kenyan workouts
    def get_kenyan_workouts(self):
        return self.kenyan
    #get long workouts
    def get_long_workouts(self):
        return self.long
    #get threshold workouts
    def get_threshold_workouts(self):
        return self.threshold\
    #get fartlek workouts
    def get_fartlek_workouts(self):
        return self.fartlek
    #get race pace interval workouts
    def get_race_pace_interval_workouts(self):
        return self.race_pace_interval
    #get strides workouts
    def get_strides_workouts(self):
        return self.strides
    #get hill sprints workouts
    def get_hill_sprints_workouts(self):
        return self.hill_sprints
    #get flat sprints workouts
    def get_flat_sprints_workouts(self):
        return self.flat_sprints
    #get time trial workouts
    def get_time_trial_workouts(self):
        return self.time_trial