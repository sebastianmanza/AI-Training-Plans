
ALPHA = 0.5  # Tuneable weighting parameter for delta RPE in difficulty calculation

def completion_score(expected_reps, observed_reps, expected_pace, observed_pace):
    """
    Calculate the completion score based on expected and observed repetitions and pace.
    
    Args:
        expected_reps (int): Expected number of repetitions (either miles or reps).
        observed_reps (int): Observed number of repetitions (either miles or reps).
        expected_pace (int): Expected pace in seconds per mile.
        observed_pace (int): Observed pace in seconds per mile.
    
    Returns:
        float: The completion score as a percentage.
    """
    
    rep_score = (observed_reps / expected_reps) - 1
    pace_score = (observed_pace / expected_pace) - 1
    
    return rep_score + pace_score

def delta_RPE(expected_RPE, observed_RPE):
    """
    Calculate the delta RPE based on expected and observed RPE values.
    
    Args:
        expected_RPE (int): Expected RPE value.
        observed_RPE (int): Observed RPE value.
    
    Returns:
        float: The delta RPE as a percentage.
    """
    
    return (observed_RPE - expected_RPE)

def delta_difficulty(comp_score, delta_rpe):
    """
    Calculate the delta difficulty based on completion score and delta RPE.
    
    Args:
        comp_score (float): Completion score.
        delta_rpe (float): Delta RPE value.
    
    Returns:
        float: The delta difficulty as a percentage.
    """
    
    return comp_score - ALPHA * delta_rpe
print(completion_score(5, 4, 360, 300))
print(delta_RPE(7, 6))