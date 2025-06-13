class day_plan: 
    __slots__ = ("total_mileage", "goal_stimuli", "pace", "rest", "lift", "expected_rpe", "real_rpe", "completion_score")
    
    def __init__(self, total_mileage: int, goal_stimuli: str, pace: int, rest: int, lift: bool, expected_rpe, real_rpe, completion_score):
        self.total_mileage = total_mileage
        self.goal_stimuli = goal_stimuli
        self.pace = pace
        self.rest = rest
        self.lift = lift
        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe
        self.completion_score = completion_score
        
        
        
        
        
        