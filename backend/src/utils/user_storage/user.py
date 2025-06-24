# import training
import math
import secrets
from backend.src.utils.user_storage.storage_stacks_and_queues import *
from backend.src.utils.time_conversion import *
from backend.src.utils.user_storage.training_database import *
from backend.src.utils.user_storage.month_plan import month_plan
from backend.src.utils.SQLutils.user_retrieve import unique_id


class user:
    # __slots__ = ("age", "sex", "five_km_estimate", "when-to-run", "injury", "mileage", "wo_history", "goal_date")
    global FIVEKDIST
    FIVEKDIST = 5000

    global CALCNUM
    CALCNUM = 1.06

    global DISTANCES
    DISTANCES = [3000, 5000, 10000]

    def __init__(self, age, sex, running_ex, five_km_estimate, goal_date, mean_RPE, STD_RPE, user_id = secrets.randbelow(100000000 - 10000000)):
        storage = storage_stacks_and_queues()
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

    def get_user_id(self):
        return self.user_id

    def generate_new_id(self):
        self.user_id = secrets.randbelow(100000000 - 10000000)

    # update training

    def update_training(self):
        self.day_future = training_database.day
        self.week_future = training_database.week
        self.month_future = training_database.month

    def update_day(self):
        self.day_future = training_database.day

    def update_week(self):
        self.week_future = training_database.week

    def update_month(self):
        self.month_future = training_database.month

    def append_month(self, month):
        self.month_history.append(month)

    def append_fut_month(self, month):
        self.month_future.put(month)

    def append_week(self, week):
        self.week_history.append(week)

    def append_fut_week(self, week):
        self.week_future.put(week)

    def append_day(self, day):
        self.day_history.append(day)

    def append_fut_day(self, day):
        self.day_future.put(day)


alex = user(19, "male", "advanced", "17:45", "3/14/2026", "5", "7")
alex.set_pace(5000, "17:30")
alex.make_predictions()
print(alex.get_user_id())
print(len(alex.times))
print(alex.get_times())
print(alex.month_history)
alex.generate_new_id()
print(alex.get_user_id())

month = month_plan(100, "Endurance", "Base", 5, 6, 100, 100, None)

# alex.append_month(month)
# alex.append_fut_month(month)
