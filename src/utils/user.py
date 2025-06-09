import training

class user: 
    __slots__ = ("age", "sex", "five_km_estimate", "when-to-run", "injury", "mileage", "wo_history", "goal_date")
    
    def __init__(self, age: int, sex: str, five_km_estimate: int, when_to_run, injury, mileage: training, wo_history: training, goal_date: str) :
        self.age = age
        self.sex = sex
        self.five_km_estimate = five_km_estimate
        self.when_to_run = when_to_run
        self.injury = injury
        self.mileage = mileage
        self.wo_history = wo_history
        self.goal_date = goal_date
        
    
        
        
        