class workout_storage:
    threshold_workouts = []
    interval_workouts = []


    ## Initialize the workout storage with empty lists for threshold and interval workouts.
    def __init__(self):
        self.threshold_workouts = []
        self.interval_workouts = []


    ## Add a workout to the appropriate list based on its type.
    ## Raises ValueError if the workout type is unknown.
    def add_workout(self, workout):
        if workout.workout_type == "Threshold":
            self.threshold_workouts.append(workout)
        elif workout.workout_type == "Interval":
            self.interval_workouts.append(workout)
        else:
            raise ValueError("Unknown workout type")

    ## Getters for the workout lists
    ## Returns the list of threshold workouts.
    def get_threshold_workouts(self):
        return self.threshold_workouts
    ## Returns the list of interval workouts.
    def get_interval_workouts(self):
        return self.interval_workouts