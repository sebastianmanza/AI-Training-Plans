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
    """return the VDOT value of a runner given the distance in meters and time in seconds."""
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
        vdot = get_VDOT(race_dist, race_time)
        target = round((MILE * 2 * 0.000104)/(-0.182258 + math.sqrt(0.182258**2 - 4 * 0.000104*(-4.6 - pct_pace * vdot))) * 60)
        return target
    


#print(get_training_pace_helper(5000, 17 * 60 + 30, RECOVERY_PCT))
