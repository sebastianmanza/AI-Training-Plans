# import training
import math
import secrets
import datetime
from backend.src.utils.user_storage.storage_stacks_and_queues import storage_stacks_and_queues
import backend.src.utils.time_conversion as tc
import backend.src.utils.user_storage.training_database as training_database


class user:
    # __slots__ = ("age", "dob", "sex", "five_km_estimate", "when-to-run", "injury", "mileage", "wo_history", "goal_date")
    global FIVEKDIST
    FIVEKDIST = 5000

    global METERS_PER_MILE
    METERS_PER_MILE = 1600

    global CALCNUM
    CALCNUM = 1.06

    global DISTANCES
    DISTANCES = [3000, 5000, 10000]

    def __init__(self, dob, sex, running_ex, five_km_estimate, goal_date, mean_RPE, STD_RPE, user_id=secrets.randbelow(100000000 - 10000000), longest_run=0):
        storage = storage_stacks_and_queues()
        self.user_id = user_id
        self.dob = dob
        self.age = self.get_age()
        self.sex = sex

        self.when_to_run = None
        self.injury = None
        self.goal_date = goal_date

        self.longest_run = longest_run
        self.running_ex = running_ex
        self.times = {}
        self.five_km_estimate_seconds = tc.mile_pace(tc.from_str(five_km_estimate), FIVEKDIST)
        self.set_pace(FIVEKDIST, self.five_km_estimate_seconds)
        self.make_predictions()
        

        self.mean_RPE = mean_RPE
        self.STD_RPE = STD_RPE

        self.month_history = storage.month_history
        self.week_history = storage.week_history
        self.day_history = storage.day_history
        self.month_future = storage.month_future
        self.week_future = storage.week_future
        self.day_future = storage.day_future

    # Takes in a distance and assigns the mile pace to it.
    def set_pace(self, distance: int, new_pace):
        if isinstance(new_pace, str):
            self.times[distance] = tc.mile_pace(new_pace, distance)
        else:
            self.times[distance] = new_pace

    # Returns the mile pace for a given distance in seconds.
    def get_pace(self, distance: int):
        return self.times[distance]

    # Makes the predictions for every distance in DISTANCES.
    def make_predictions(self):
        for distance in DISTANCES:
            self.set_pace(distance, self.predict_pace(distance))

    # Predicts the mile pace for a given distance based on the 5k pace.
    def predict_pace(self, distance):
        fivekpace = self.get_pace(FIVEKDIST)
        return math.floor((fivekpace)*pow((distance/FIVEKDIST), CALCNUM)*(FIVEKDIST / distance))

    # Returns the mile pace for each distance.
    def get_times(self):
        toReturn = ""
        for k, v in self.times.items():
            toReturn += f"{k}:{tc.to_str(v)}\n"
        return toReturn

    def get_user_id(self):
        return self.user_id

    def generate_new_id(self):
        self.user_id = secrets.randbelow(100000000 - 10000000)

    def get_age(self):
        today = datetime.date.today()
        dob = datetime.datetime.strptime(self.dob, "%m/%d/%Y").date()
        age = today.year - dob.year - \
            ((today.month, today.day) < (dob.month, dob.day))
        return age

    # update training

    # def update_training(self):
    #     self.day_future = training_database.day
    #     self.week_future = training_database.week
    #     self.month_future = training_database.month

    # def update_day(self):
    #     self.day_future = training_database.day

    # def update_week(self):
    #     self.week_future = training_database.week

    # def update_month(self):
    #     self.month_future = training_database.month

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

        # Takes in a string and a user i.e. (5000+10, 17:30 5k runner) and returns the pace associated with it.

    def parse_pace(self, pace: str):
        if pace.find("+") != -1:
            distance, increase = pace.split("+")
            increase = int(increase)
        elif pace.find("-") != -1:
            distance, increase = pace.split("-")
            increase = -int(increase)
        else:
            increase = 0
        pace = pace.strip()
        seconds = self.get_pace(int(distance))
        return tc.alter_pace(seconds, increase)


alex = user("8/22/2005", "male", "advanced", "17:30", "5", "7", "1")
print(alex.get_pace(10000))
print(alex.parse_pace("10000+10"))
# alex.set_pace(5000, "17:30")
# alex.make_predictions()
# print(alex.get_times())
# print(alex.get_user_id())
# print(len(alex.times))
# print(alex.get_times())
# print(alex.month_history)
# alex.generate_new_id()
# print(alex.get_user_id())

# month = month_plan(100, "Endurance", "Base", 5, 6, 100, 100, None)

# alex.append_month(month)
# alex.append_fut_month(month)
