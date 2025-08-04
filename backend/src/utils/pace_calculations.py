import math

MILE = 1609.34  # Meters in a mile


RECOVERY_PCT = 0.64
EASY_PCT = 0.67
TEMPO_PCT = 0.82
THRESH_PCT = 0.87
VO2MAX_PCT = 0.95
TIME_CONVERSION_NUM = 60
# Pace calculation functions:


@staticmethod
def get_VDOT(dist: float, time: float) -> float:
    """Return the VDOT value of a runner.

    Args:
        dist (float): Distance in meters.
        time (float): Time in seconds.

    Returns:
        float: Calculated VDOT value.

    Raises:
        ValueError: If ``dist`` or ``time`` are non-positive.
    """
    if dist <= 0 or time <= 0:
        raise ValueError("Distance and time must be positive values.")
    time_min = time / 60  # Convert time to minutes
    vel = dist / time_min  # Velocity in meters per minute

    vo2 = -4.6 + 0.182258 * vel + 0.000104 * vel ** 2
    percent_max = 0.8 + 0.1894393 * \
        math.exp(-0.012778 * time_min) + 0.2989558 * \
        math.exp(-0.1932605 * time_min)

    vdot = vo2 / percent_max
    return vdot


@staticmethod
def get_training_pace_helper(race_dist: float, race_time: float, pct_pace: float) -> float:
    """Calculate a target pace from race performance.

    Args:
        race_dist (float): Race distance in meters.
        race_time (float): Completion time in seconds.
        pct_pace (float): Desired training pace as a percentage of VDOT pace.

    Returns:
        float: Target pace in seconds per mile.
    """
    vdot = get_VDOT(race_dist, race_time)
    target = round((MILE * 2 * 0.000104)/(-0.182258 + math.sqrt(0.182258 **
                   2 - 4 * 0.000104*(-4.6 - pct_pace * vdot))) * 60)
    return target


# print(get_training_pace_helper(5000, 17 * 60 + 30, RECOVERY_PCT))


# Time conversion functions:


@staticmethod
def to_str(sec: int) -> str:
    """Convert seconds to ``H:MM:SS`` format.

    Args:
        sec (int): Number of seconds.

    Returns:
        str: Time string.
    """
    minutes = (math.floor(sec/TIME_CONVERSION_NUM) %
               TIME_CONVERSION_NUM)  # Get the number of minutes
    hours = math.floor(sec/(TIME_CONVERSION_NUM*TIME_CONVERSION_NUM)
                       )  # Get the number of hours
    remainingSec = sec % TIME_CONVERSION_NUM  # Get the seconds
    toReturn = ""
    if hours != 0:  # Check to add hours
        toReturn += f"{hours}:"
    if minutes != 0:  # Check to add minutes
        toReturn += f"{minutes}:"
    toReturn += f"{remainingSec:02d}"  # Always add seconds
    return toReturn


@staticmethod
def from_str(pace: str) -> int:
    """Convert pace from ``H:MM:SS`` format to seconds.

    Args:
        pace (str): Pace string.

    Returns:
        int: Total seconds.
    """
    times = pace.split(":")  # Split the string to
    multiplier = 1  # Prepare the multiplier for conversion
    total = 0  # Total seconds
    for num in reversed(times):  # Go through the times to convert to seconds
        # Add the time to the total when changed by the multiplier
        total += multiplier * int(num)
        multiplier *= TIME_CONVERSION_NUM  # Increase the multiplier for the next time
    return total


@staticmethod
def from_dec(pace: float) -> str:
    """Convert decimal pace to ``M:SS`` string."""
    dec = math.floor(
        (pace % 1) * TIME_CONVERSION_NUM)  # Get the decimal part in seconds
    val = math.floor(pace)  # Get the integer part in minutes
    return f"{val}:{dec}"


@staticmethod
def total_time_miles(pace, mile: int) -> int:
    """Return total time for ``mile`` miles at ``pace`` seconds per mile.

    Args:
        pace (int | str): Pace in seconds or ``H:MM:SS`` format.
        mile (int): Distance in miles.

    Returns:
        int: Total time in seconds.
    """
    if isinstance(pace, str):  # If pace is a string, convert it to seconds
        pace = from_str(pace)
    return total_time(pace, (mile * MILE))


@staticmethod
def total_time(pace, distance: int) -> int:
    """Return total time for ``distance`` meters at ``pace`` seconds per mile.

    Args:
        pace (int | str): Pace in seconds or ``H:MM:SS`` format.
        distance (int): Distance in meters.

    Returns:
        int: Time in seconds.
    """
    if isinstance(pace, str):  # If pace is a string, convert it to seconds
        pace = from_str(pace)
    return math.floor((pace * distance) / MILE)


@staticmethod
def mile_pace(pace, distance: int) -> int:
    """Return the pace per mile for a given distance.

    Args:
        pace (int | str): Pace in seconds or ``H:MM:SS`` format.
        distance (int): Distance in meters.

    Returns:
        int: Pace in seconds per mile.
    """
    if distance == 0:  # If distance is 0, return 0 to avoid division by zero
        return 0
    if isinstance(pace, str):  # If pace is a string, convert it to seconds
        pace = from_str(pace)
    return math.floor((pace * MILE) / distance)

# Addtional functions:


@staticmethod
def average_property(list_to_average: list,  property_name: str) -> float:
    """Calculate the average of a specific property from a list of objects."""
    total = 0
    for item in list_to_average:
        try:
            total += getattr(item, property_name)
        except AttributeError:
            raise ValueError(
                f"Item {item} does not have property '{property_name}'")
    return total / len(list_to_average) if list_to_average else 0

# print(parse_pace("5000-10", "17:30 5k runner"))  # Example (to use replace seconds = user.get_pace(int(distance)) with seconds = "17:30")
# print(get_training_pace_helper(5000, 17 * 60 + 30, RECOVERY_PCT))
