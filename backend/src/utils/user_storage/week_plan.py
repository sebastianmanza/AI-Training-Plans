import backend.src.utils.user_storage.day_plan as day_plan 

class week_plan:
    __slots__ = ("total_mileage", "goal_stimuli", "cycle", "expected_rpe", "real_rpe", "completion_score", "daily_id")
    
    def __init__(self, total_mileage: int, goal_stimuli: str, cycle: str, expected_rpe, real_rpe, completion_score, daily_id: day_plan):
        self.total_mileage = total_mileage
        self.goal_stimuli = goal_stimuli
        self.cycle = cycle
        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe
        self.completion_score = completion_score