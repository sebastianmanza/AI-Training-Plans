import workout_node

# A simple wrapper class meant to add the type of workout to it's information


class workout:
    def __init__(self, workout: workout_node, aerobicVspeed: float, stressorVrecovery: float):
        self.workout = workout
        self.aerobicVspeed = aerobicVspeed  # Aerobic speed in m/s
        self.stressorVrecovery = stressorVrecovery

    def __str__(self):
        toReturn = ""
        if (self.aerobicVspeed < 0):
            toReturn += f"aerobic({self.aerobicVspeed})/"
        else:
            toReturn += f"speed({self.aerobicVspeed})/"
        if (self.stressorVrecovery < 0):
            toReturn += f"recovery({self.stressorVrecovery})"
        else:
            toReturn += f"stressor({self.stressorVrecovery})"
        return toReturn

    def get_aerobicVspeed(self):
        return self.aerobicVspeed

    def set_aerobicVspeed(self, aerobicVspeed):
        self.aerobicVspeed = aerobicVspeed

    def get_stressorVrecovery(self):
        return self.stressorVrecovery

    def set_stressorVrecovery(self, stressorVrecovery):
        self.stressorVrecovery = stressorVrecovery

    def get_workout(self):
        return self.workout

    def set_workout(self, workout):
        self.workout = workout


new_workout = workout(None, -1, 1)
print(new_workout)
