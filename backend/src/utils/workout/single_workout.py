

class single_workout:

    __slots__ = ("trio", "reps", "pace", "distance")

    # trio = x, y, z = (stim, RPE, distance)
    # reps = list of ints (in meters)
    # pace = list of strings (pace type: 5k, easy, mile, etc.)
    # distance = % of total long run distance (1-100)
    def __init__(self, trio, reps = list, pace = list, distance = int):
        self.trio = trio
        self.reps = reps
        self.pace = pace
        self.distance = distance

    