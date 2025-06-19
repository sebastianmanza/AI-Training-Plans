from backend.src.utils.workout.workout_storage import *

class workout_database:

    storage = workout_storage()

    def __init__(self, et = list, recovery = list, kenyan = list, 
                 long = list, threshold = list, fartlek = list,
                 race_pace_interval = list, strides = list, hill_sprints = list,
                 flat_sprints = list, time_trial = list, warmup_and_cooldown = list):
        
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