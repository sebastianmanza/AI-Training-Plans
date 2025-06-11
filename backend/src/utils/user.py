# import training

class user:
    # __slots__ = ("age", "sex", "five_km_estimate", "when-to-run", "injury", "mileage", "wo_history", "goal_date")

    def __init__(self, age, sex, running_ex, five_km_estimate, goal_date,):
        self.age = age
        self.sex = sex
        self.five_km_estimate = five_km_estimate
        self.when_to_run = None
        self.injury = None
        self.mileage = None
        self.wo_history = None
        self.goal_date = goal_date
        self.running_ex = running_ex
        self.times = {}

    def set_pace(self, distance: int, new_pace: str):
        self.times.update({distance: new_pace})

    def get_pace(self, distance: int):
        return self.times[distance]


alex = user(19, "male", "advanced", "17:45", "3/14/2026")
alex.set_pace(800, "2:00")
alex.set_pace(800, "2:15")
alex.set_pace(200, "2:15")
print(len(alex.times))
print(alex.get_pace(800))
