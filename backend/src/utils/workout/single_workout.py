TRIO_STIM, TRIO_RPE, TRIO_DIST = 0, 1, 2


class single_workout:

    __slots__ = ("trio", "reps", "pace", "distance")

    # trio = x, y, z = (stim, RPE, distance)
    # reps = list of ints (in meters)
    # pace = list of strings (pace type: 5k, easy, mile, etc.)
    # distance = % of total long run distance (1-100)
    def __init__(self, trio: tuple, reps: list, pace: list, distance: int):
        self.trio = trio
        self.reps = reps
        self.pace = pace
        self.distance = distance

    def get_trio(self) -> tuple:
        return self.trio

    def get_stim(self) -> float:
        """Return the stimulus"""
        return self.trio[TRIO_STIM]

    def get_rpe(self) -> float:
        """Return the RPE"""
        return self.trio[TRIO_RPE]

    def get_distance(self) -> float:
        """"Return the distance"""
        return self.trio[TRIO_DIST]

    def get_pace(self) -> list:
        """Return the pace"""
        return self.pace

    def get_reps(self) -> list:
        """Return the reps"""
        return self.reps

    def __str__(self) -> str:
        return f"Workout: {self.trio}, Reps: {self.reps}, Pace: {self.pace}, Distance: {self.distance}"
