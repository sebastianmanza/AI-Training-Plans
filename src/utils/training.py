import day_plan, month_plan, week_plan

class training:
    __slots__ = ("daily", "weekly", "monthly")
    
    def __init__(self, daily: day_plan, weekly: week_plan, monthly: month_plan):
        self.daily = daily
        self.weekly = weekly
        self.monthly = monthly
        
        
