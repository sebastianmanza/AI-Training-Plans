import workout_node

# A simple wrapper class meant to add the type of workout to it's information


class workout:
    def __init__(self, workout: workout_node, aerobicVspeed: float, recoveryVstressor: float):
        self.workout = workout
        self.aerobicVspeed = aerobicVspeed  # Negative for aerobic, positive for speed
        # Negative for recovery, positive for stressor.
        self.recoveryVstressor = recoveryVstressor

    def __str__(self):
        toReturn = ""
        if (self.aerobicVspeed < 0):
            toReturn += f"aerobic({self.aerobicVspeed})/"
        else:
            toReturn += f"speed({self.aerobicVspeed})/"
        if (self.recoveryVstressor < 0):
            toReturn += f"recovery({self.recoveryVstressor})"
        else:
            toReturn += f"stressor({self.recoveryVstressor})"
        return toReturn

    def get_aerobicVspeed(self):
        return self.aerobicVspeed

    def set_aerobicVspeed(self, aerobicVspeed):
        self.aerobicVspeed = aerobicVspeed

    def get_stressorVrecovery(self):
        return self.recoveryVstressor

    def set_stressorVrecovery(self, recoveryVstressor):
        self.recoveryVstressor = recoveryVstressor

    def get_workout(self):
        return self.workout

    def set_workout(self, workout):
        self.workout = workout
