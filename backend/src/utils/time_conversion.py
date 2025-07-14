import math


METERS_PER_MILE = 1609
CONVERSION_NUM = 60


def to_str(sec: int) -> str:
    """ Convert seconds to a string in the format H:MM:SS."""
    minutes = (math.floor(sec/CONVERSION_NUM) %
               CONVERSION_NUM)  # Get the number of minutes
    hours = math.floor(sec/(CONVERSION_NUM*CONVERSION_NUM)
                       )  # Get the number of hours
    remainingSec = sec % CONVERSION_NUM  # Get the seconds
    toReturn = ""
    if hours != 0:  # Check to add hours
        toReturn += f"{hours}:"
    if minutes != 0:  # Check to add minutes
        toReturn += f"{minutes}:"
    toReturn += f"{remainingSec:02d}"  # Always add seconds
    return toReturn


def from_str(pace: str) -> int:
    """ Convert pace in the format H:MM:SS to seconds."""
    times = pace.split(":")  # Split the string to
    multiplier = 1  # Prepare the multiplier for conversion
    total = 0  # Total seconds
    for num in reversed(times):  # Go through the times to convert to seconds
        # Add the time to the total when changed by the multiplier
        total += multiplier * int(num)
        multiplier *= CONVERSION_NUM  # Increase the multiplier for the next time
    return total


def from_dec(pace: float) -> str:
    """ Convert decimal pace to a string in the format M:SS."""
    dec = math.floor(
        (pace % 1) * CONVERSION_NUM)  # Get the decimal part in seconds
    val = math.floor(pace)  # Get the integer part in minutes
    return f"{val}:{dec}"

# This is essentially a helper function


def total_time_miles(pace, mile: int) -> int:
    """ Calculate the total time in seconds for a given pace (in seconds per mile) and distance (in miles)."""
    if isinstance(pace, str):  # If pace is a string, convert it to seconds
        pace = from_str(pace)
    return total_time(pace, (mile * METERS_PER_MILE))


def total_time(pace, distance: int) -> int:
    """ Calculate the total time in seconds for a given pace (in seconds per mile) and distance (in meters)."""
    if isinstance(pace, str):  # If pace is a string, convert it to seconds
        pace = from_str(pace)
    return math.floor((pace * distance) / METERS_PER_MILE)


def alter_pace(pace, increase: int) -> int:
    """ Alter the pace by a given increase in seconds."""
    if isinstance(pace, str):  # If pace is a string, convert it to seconds
        pace = from_str(pace)
    return pace + increase


def mile_pace(pace, distance: int) -> int:
    if distance == 0:  # If distance is 0, return 0 to avoid division by zero
        return 0
    if isinstance(pace, str):  # If pace is a string, convert it to seconds
        pace = from_str(pace)
    return math.floor((pace * METERS_PER_MILE) / distance)


# print(parse_pace("5000-10", "17:30 5k runner"))  # Example (to use replace seconds = user.get_pace(int(distance)) with seconds = "17:30")
