import math


class timeConversion:
    global METERS_PER_MILE
    METERS_PER_MILE = 1609
    global MIN_CONVERSION
    MIN_CONVERSION = 60

    def __init__(self):
        pass

    # Convert from seconds to string 1:01:01 -> whatever that is in seconds
    def to_str(sec: int):
        minutes = (math.floor(sec/MIN_CONVERSION) % MIN_CONVERSION)
        hours = math.floor(sec/(MIN_CONVERSION*MIN_CONVERSION))
        remainingSec = sec % MIN_CONVERSION
        toReturn = ""
        if hours != 0:
            toReturn += f"{hours}:"
        if minutes != 0:
            toReturn += f"{minutes}:"
        toReturn += f"{remainingSec}"
        return toReturn

    # Convert from pace (as string) to seconds 1:10->70
    def from_str(pace: str):
        times = pace.split(":")
        multiplier = 1
        total = 0
        for num in reversed(times):
            total += multiplier*int(num)
            multiplier *= MIN_CONVERSION
        return total

    # Convert from decimal to pace. i.e. 7.5->7:30
    def from_dec(pace: int):
        dec = math.floor((pace % 1)*MIN_CONVERSION)
        val = math.floor(pace)
        return f"{val}:{dec}"

    def total_time_miles(pace: str, mile: int):
        converter = timeConversion
        return converter.total_time(pace, (mile*METERS_PER_MILE))

    def total_time(pace: str, distance: int):
        converter = timeConversion
        sec = math.floor(((converter.from_str(pace))*distance)/METERS_PER_MILE)
        return converter.to_str(sec)


converter = timeConversion
print(converter.total_time_miles("7:30", 2))
