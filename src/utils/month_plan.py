import week_plan

class month_plan:
    __slots__ = ("total_mileage", "goal_stimuli", "cycle", "expected_rpe", "real_rpe", "completion_score", "week_id")
    
    def __init__(self, total_mileage: int, goal_stimuli: str, cycle: str, expected_rpe, real_rpe, completion_score, week_id: week_plan):
        self.total_mileage = total_mileage
        self.goal_stimuli = goal_stimuli
        self.cycle = cycle
        self.expected_rpe = expected_rpe
        self.real_rpe = real_rpe
        self.completion_score = completion_score
        self.week_id = week_id