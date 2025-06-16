import math


global METERS_PER_MILE
METERS_PER_MILE = 1609
global MIN_CONVERSION
MIN_CONVERSION = 60

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
        total += multiplier * int(num)
        multiplier *= MIN_CONVERSION
    return total

# Convert from decimal to pace. i.e. 7.5->7:30


def from_dec(pace: float):
    dec = math.floor((pace % 1) * MIN_CONVERSION)
    val = math.floor(pace)
    return f"{val}:{dec}"

# Convert from distance and pace to total time


def total_time_miles(pace: str, mile: int):
    return total_time(pace, (mile * METERS_PER_MILE))


def total_time(pace: str, distance: int):
    sec = math.floor((from_str(pace) * distance) / METERS_PER_MILE)
    return to_str(sec)

# Alter the pace and return it as a string. Remember you can add negative numbers


def alter_pace(pace: str, increase: int):
    return to_str(from_str(pace) + increase)
