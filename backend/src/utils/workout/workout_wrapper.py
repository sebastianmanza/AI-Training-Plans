class workout_wrapper:

    __slots__ = ("trio", "workout")

    def __init__(self, trio, workout):
        self.trio = trio
        self.workout = workout
    
    # Returns the trio associated with the workout.
    def get_trio(self):
        return self.trio
    
    # Returns the workout associated with a given trio.
    def get_workout(self):
        return self.workout