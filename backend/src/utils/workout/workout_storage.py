from backend.src.utils.workout.workout_type_library import *

class workout_storage:
    #all the workout types
    ## These lists will store different types of workouts.
    ## lists of key value points that the key is the trio and the value is the workout
    __slots__ = ("et", "recovery", "kenyan", "long", "threshold", "fartlek", "race_pace_interval",
                    "strides", "hill_sprints", "flat_sprints", "time_trial", "warmup_and_cooldown")


    ## Initialize the workout storage with empty lists for threshold and interval workouts.
    def __init__(self):
        self.et = []
        self.recovery = []
        self.kenyan = []
        self.long = []
        self.threshold = []
        self.fartlek = []
        self.race_pace_interval = []
        self.strides = []
        self.hill_sprints = []
        self.flat_sprints = []
        self.time_trial = []
        self.warmup_and_cooldown = []


    ## Add a workout to the appropriate list based on its type.
    ## Raises ValueError if the workout type is unknown.
    def add_workout(self, workout):
        for key in workout_type_library.workout_dictionary:
            final_type = workout_type_library.get_workout_type(workout[0][0], workout[0][1], workout[0][2])
            self.final_type.append(workout)

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
    #get warmup and cooldown workouts
    def get_warmup_and_cooldown(self):
        return self.warmup_and_cooldown