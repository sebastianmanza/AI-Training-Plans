import math


class timeConversion:

    def __init__(self):
        pass

    def to_str(sec: int):
        minutes = (math.floor(sec/60) % 60)
        hours = math.floor(sec/(60*60))
        remainingSec = sec % 60
        toReturn = ""
        if hours != 0:
            toReturn += f"{hours}:"
        toReturn += f"{minutes}:{remainingSec}"
        return toReturn

    def from_str(pace: str):
        times = pace.split(":")
        multiplier = 1
        total = 0
        for num in reversed(times):
            total += multiplier*int(num)
            multiplier *= 60
        return total


s2s = timeConversion
print(s2s.from_str("1:11:12"))
