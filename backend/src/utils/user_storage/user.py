# import training
import math
from backend.src.utils.user_storage.storage_stacks_and_queues import *
from backend.src.utils.time_conversion import *


class user:
    # __slots__ = ("age", "sex", "five_km_estimate", "when-to-run", "injury", "mileage", "wo_history", "goal_date")
    global FIVEKDIST
    FIVEKDIST = 5000

    global CALCNUM
    CALCNUM = 1.06

    global DISTANCES
    DISTANCES = [3000, 5000, 10000]

    def __init__(self, user_id, age, sex, running_ex, five_km_estimate, goal_date, mean_RPE, STD_RPE):
        storage = storage_stacks_and_queues
        self.user_id = user_id
        self.age = age
        self.sex = sex
        self.five_km_estimate = five_km_estimate
        self.when_to_run = None
        self.injury = None
        self.goal_date = goal_date
        self.running_ex = running_ex
        self.times = {}
        self.mean_RPE = mean_RPE
        self.STD_RPE = STD_RPE
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
        fivekpace = from_str(self.get_pace(FIVEKDIST))
        return to_str(math.floor((fivekpace)*pow((distance/FIVEKDIST), CALCNUM)))

    def get_times(self):
        toReturn = ""
        for k, v in self.times.items():
            toReturn += f"{k}:{v}\n"
        return toReturn


