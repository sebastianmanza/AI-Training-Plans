class single_workout:

    __slots__ = ("trio", "reps", "pace", "distance")

    # trio = x, y, z = (stim, RPE, distance)
    # reps = list of ints (in meters)
    # pace = list of strings (pace type: 5k, easy, mile, etc.)
    # distance = % of total long run distance (1-100)
    def __init__(self, trio, reps=list, pace=list, distance=int):
        self.trio = trio
        self.reps = reps
        self.pace = pace
        self.distance = distance

    def get_trio(self):
        return self.trio

    def get_stim(self):
        """Return the stimulus"""
        return self.trio[0]

    def get_rpe(self):
        """Return the RPE"""
        return self.trio[1]

    def get_distance(self):
        """"Return the distance"""
        return self.trio[2]

    def __str__(self):
        return f"Workout: {self.trio}, Reps: {self.reps}, Pace: {self.pace}, Distance: {self.distance}"
