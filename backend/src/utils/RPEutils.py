
ALPHA = 0.5  # Tuneable weighting parameter for delta RPE in difficulty calculation
POW = 3  # Power for pace rating normalization in completion score calculation
DIVISOR = 125  # Divisor for pace rating normalization in completion score calculation


def completion_score(expected_reps: int, observed_reps: int, pace_rating: int) -> float:
    """
    Calculate the completion score based on expected and observed repetitions and pace.

    Args:
        expected_reps (int): Expected number of repetitions (either miles or reps).
        observed_reps (int): Observed number of repetitions (either miles or reps).
        pace_rating (int): The users average pace compared to expected (-5 for slower, 0 for same, 5 for faster).
    Returns:
        float: The completion score as a percentage.
    """

    rep_score = float((observed_reps / expected_reps) - 1)
    pace_score = pow(pace_rating, POW)/DIVISOR

    return rep_score + pace_score


def delta_RPE(expected_RPE: int, observed_RPE: int) -> int:
    """
    Calculate the delta RPE based on expected and observed RPE values.

    Args:
        expected_RPE (int): Expected RPE value.
        observed_RPE (int): Observed RPE value.

    Returns:
        int: The delta RPE
    """

    return (observed_RPE - expected_RPE)


def delta_difficulty(comp_score: float, delta_rpe: float) -> float:
    """
    Calculate the delta difficulty based on completion score and delta RPE.

    Args:
        comp_score (float): Completion score.
        delta_rpe (float): Delta RPE value.

    Returns:
        float: The delta difficulty as a percentage.
    """

    return comp_score - ALPHA * delta_rpe


score = completion_score(5, 5, 6)
print(score)
print(delta_RPE(7, 6))
