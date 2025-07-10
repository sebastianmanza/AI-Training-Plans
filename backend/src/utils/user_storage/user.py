# import training
import math
import secrets
import datetime
from backend.src.utils.user_storage.storage_stacks_and_queues import storage_stacks_and_queues
import backend.src.utils.time_conversion as tc
import backend.src.utils.user_storage.training_database as training_database
from backend.src.utils.pace_calculations import get_training_pace_helper

FIVEKDIST, METERS_PER_MILE = 5000, 1600  # Distance conversions
CALCNUM = 1.06  # Exponent for pace prediction
DISTANCES = [3000, 5000, 10000]  # Distances for which we will make predictions
RPE, DAYS, DEVIATION = 0, 1, 2  # Indexes used for mean RPE
DEFAULT_WORKOUT_NUMS = {
    "Easy Run": (0, 0, 0), "Recovery Run": (0, 0, 0), "Progression": (0, 0, 0), "Long Run": (0, 0, 0),
    "Threshold": (0, 0, 0), "Fartlek": (0, 0, 0), "Race Pace Interval": (0, 0, 0), "Strides": (0, 0, 0),
    "Hill Sprints": (0, 0, 0), "Flat Sprints": (0, 0, 0), "Time Trial": (0, 0, 0), "Warmup and Cooldown": (0, 0, 0), "Off": (0, 0, 0)}


class user:
    # __slots__ = ("age", "dob", "sex", "five_km_estimate", "when-to-run", "injury", "mileage", "wo_history", "goal_date")

    def __init__(self, dob, sex: str, running_ex, five_km_estimate: str, goal_date, mean_RPE: float,
                 STD_RPE: float, user_id=secrets.randbelow(100000000 - 10000000), longest_run: int = 0,
                 workout_nums=DEFAULT_WORKOUT_NUMS):
        storage = storage_stacks_and_queues()
        self.user_id = user_id
        self.dob = dob
        # self.age = self.get_age()
        self.sex = sex

        self.when_to_run = None
        self.injury = 0
        self.most_recent_injury = 0

        self.goal_date = goal_date

        self.longest_run = longest_run
        self.running_ex = running_ex
        self.pace_times_dict = {}
<<<<<<< HEAD
        # self.five_km_estimate_seconds = tc.mile_pace(
        #     tc.from_str(five_km_estimate), FIVEKDIST)
        # self.set_pace(FIVEKDIST, self.five_km_estimate_seconds)
        # self.make_predictions()
        self.five_km_estimate_seconds = five_km_estimate
=======
        self.five_km_estimate_seconds = tc.mile_pace(
            tc.from_str(five_km_estimate), FIVEKDIST)
        # self.set_pace(FIVEKDIST, self.five_km_estimate_seconds)
        # self.make_predictions()
        # self.five_km_estimate_seconds = five_km_estimate
>>>>>>> 15b89316ba5e461379bbca3c4a554a5cd240fb74

        self.mean_RPE = mean_RPE
        self.STD_RPE = STD_RPE

        self.month_history = storage.month_history
        self.week_history = storage.week_history
        self.day_history = storage.day_history
        self.month_future = storage.month_future
        self.week_future = storage.week_future
        self.day_future = storage.day_future

        # The key is the type of run. The first number in the value is the mean RPE
        # and the second is the number of these workouts run.
        # the third number is the average deviation
        # i.e.(5,2,1) implies the mean RPE is 5 after 2 workouts with an average deviation of 1
        self.workout_mean_RPE = workout_nums

    # Update the mean_RPE using the workout type and the RPE

    def update_mean_RPE(self, type: str, given_RPE: float, expected_RPE: float) -> None:
        # Get the info for the workout type
        info = self.workout_mean_RPE.get(type)
        new_mean = ((info[RPE]*info[DAYS]) + given_RPE) / \
            (info[DAYS]+1)  # Calculate the new mean
        # Calculate the new average deviation
        new_deviation = ((info[DEVIATION]*info[DAYS]) +
                         abs(given_RPE-expected_RPE)) / (info[DAYS]+1)
        self.workout_mean_RPE.update(
            type, (new_mean, (info[DAYS]+1)))  # Update the information

    # Takes in a distance and assigns the mile pace to it.

    def set_pace(self, distance: int, new_pace) -> None:
        if isinstance(new_pace, str):
            self.pace_times_dict[distance] = tc.mile_pace(new_pace, distance)
        else:
            self.pace_times_dict[distance] = new_pace

    # Returns the mile pace for a given distance in seconds.
    def get_pace(self, distance: int) -> int:
        return self.pace_times_dict[distance]

    # Makes the predictions for every distance in DISTANCES.
    def make_predictions(self) -> None:
        for distance in DISTANCES:
            self.set_pace(distance, self.predict_pace(distance))

    # Predicts the mile pace for a given distance based on the 5k pace.
    def predict_pace(self, distance) -> int:
        fivekpace = self.get_pace(FIVEKDIST)
        return math.floor((fivekpace)*pow((distance/FIVEKDIST), CALCNUM)*(FIVEKDIST / distance))

    # Returns the mile pace for each distance.
    def get_times(self) -> str:
        toReturn = ""
        for k, v in self.pace_times_dict.items():
            toReturn += f"{k}:{tc.to_str(v)}\n"
        return toReturn

    def get_user_id(self) -> int:
        return self.user_id

    def generate_new_id(self) -> None:
        self.user_id = secrets.randbelow(100000000 - 10000000)

    # def get_age(self) -> int:
    #     """Returns the number of years the user has been alive as an int"""
    #     today = datetime.date.today()
    #     dob = datetime.datetime.strptime(self.dob, "%m/%d/%Y").date()
    #     age = today.year - dob.year - \
    #         ((today.month, today.day) < (dob.month, dob.day))
    #     return age

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

    def parse_pace(self, pace: str) -> int:
        if pace.find("+") != -1:  # See if a value is being added
            distance, increase = pace.split("+")
            increase = int(increase)
        elif pace.find("-") != -1:  # See if a value is being subtracted
            distance, increase = pace.split("-")
            increase = -int(increase)
        else:  # No increase
            distance, increase = pace, 0
        pace = pace.strip()
        seconds = self.get_pace(int(distance))
        return tc.alter_pace(seconds, increase)

    def get_training_pace(self, type) -> int:
        """Returns the training pace for a given type of workout."""
        if type == "Easy Run":
            return get_training_pace_helper(5000, self.five_km_estimate_seconds * 3.1, 0.67)
        elif type == "Progression":
            return get_training_pace_helper(5000, self.five_km_estimate_seconds * 3.1, 0.82)
        elif type == "Recovery Run":
            return get_training_pace_helper(5000, self.five_km_estimate_seconds * 3.1, 0.64)
        elif type == "Threshold":
            return get_training_pace_helper(5000, self.five_km_estimate_seconds * 3.1, 0.87)
        elif type == "Long Run":
            return get_training_pace_helper(5000, self.five_km_estimate_seconds * 3.1, 0.7)
        elif type == "VO2Max":
            return get_training_pace_helper(5000, self.five_km_estimate_seconds * 3.1, 0.95)
        elif type == "Tempo":
            return get_training_pace_helper(5000, self.five_km_estimate_seconds * 3.1, 0.82)
        else:
            return 0

# alex = user("8/22/2005", "male", "advanced", "17:30", "5", "7", "1")
# # print(alex.get_pace(10000))
# # print(alex.parse_pace("10000"))

# print(alex.five_km_estimate_seconds)
# print(alex.get_training_pace("Recovery Run"))

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