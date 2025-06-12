# import training
import storage_stacks_and_queues
import math
from time_conversion import *


class user:
    # __slots__ = ("age", "sex", "five_km_estimate", "when-to-run", "injury", "mileage", "wo_history", "goal_date")
    global FIVEKDIST
    FIVEKDIST = 5000

    global CALCNUM
    CALCNUM = 1.06

    global DISTANCES
    DISTANCES = [3000, 5000, 10000]

    def __init__(self, age, sex, running_ex, five_km_estimate, goal_date):
        storage = storage_stacks_and_queues.storage_stacks_and_queues
        self.age = age
        self.sex = sex
        self.five_km_estimate = five_km_estimate
        self.when_to_run = None
        self.injury = None
        self.goal_date = goal_date
        self.running_ex = running_ex
        self.times = {}
        self.month_history = storage.month_history
        self.week_history = storage.week_history
        self.day_history = storage.day_history
        self.month_future = storage.month_future
        self.week_future = storage.week_future
        self.day_future = storage.day_future
        
        

    def set_pace(self, distance: int, new_pace: str):
        self.times[distance] = new_pace

    def get_pace(self, distance: int):
        return self.times[distance]

    def make_predictions(self):
        for distance in DISTANCES:
            self.set_pace(distance, self.predict_distance(distance))

    def predict_distance(self, distance):
        fivekpace = time_conversion.from_str(self.get_pace(FIVEKDIST))
        return time_conversion.to_str(math.floor((fivekpace)*pow((distance/FIVEKDIST), CALCNUM)))

    def get_times(self):
        toReturn = ""
        for k, v in self.times.items():
            toReturn += f"{k}:{v}\n"
        return toReturn


alex = user(19, "male", "advanced", "17:45", "3/14/2026")
alex.set_pace(5000, "17:30")
alex.make_predictions()
print(len(alex.times))
print(alex.get_times())
