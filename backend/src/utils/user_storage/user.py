# import training
import logging
import math
import secrets
import datetime
from backend.src.utils.user_storage.storage_stacks_and_queues import storage_stacks_and_queues
import backend.src.utils.time_conversion as tc
import backend.src.utils.user_storage.training_database as training_database
from backend.src.utils.pace_calculations import get_training_pace_helper
from backend.src.utils.SQLutils.database_connect import init_db


FIVEKDIST, METERS_PER_MILE = 5000, 1600  # Distance conversions
CALCNUM = 1.06  # Exponent for pace prediction
DISTANCES = [3000, 5000, 10000]  # Distances for which we will make predictions
RPE, DAYS, DEVIATION = 0, 1, 2  # Indexes used for mean RPE
DEFAULT_WORKOUT_NUMS = {
    "Easy Run": (0, 0, 0), "Recovery Run": (0, 0, 0), "Progression": (0, 0, 0), "Long Run": (0, 0, 0),
    "Threshold": (0, 0, 0), "Fartlek": (0, 0, 0), "Race Pace Interval": (0, 0, 0), "Strides": (0, 0, 0),
    "Hill Sprints": (0, 0, 0), "Flat Sprints": (0, 0, 0), "Time Trial": (0, 0, 0), "Warmup and Cooldown": (0, 0, 0), "Off": (0, 0, 0)}

THREEK, FIVEK, TENK, RECOVERY, EASY, TEMPO, PROGRESSION, THRESHOLD, LONGRUN, VO2MAX = range(10)

class user:
    # __slots__ = ("dob", "sex", "running_ex", "injury", "most_recent_injury", "longest_run", "goal_date", "pace_estimates", "available_days", "number_of_days", "user_id", "workout_RPE")

    def __init__(self, dob: str, sex: str, running_ex: str, injury: int, most_recent_injury: int, longest_run: int,  goal_date: str, 
                available_days: list, number_of_days: int, pace_estimates: list = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], user_id: int = secrets.randbelow(90000000) + 10000000, workout_RPE=DEFAULT_WORKOUT_NUMS):
        """Creates a user from the given arguments and initializes storage which is the series of stacks and queues necessary for 
        storing all past and future workouts from a training plan for the user.
        Args:
            self: The user
            dob: --string: The users date of birth
            sex: --string: The users sex
            running_ex: --string: The users running level
            injury: --int: How many injuries a user has had in the last 2 years
            most_recent_injury: --int: The number of months ago the users most recent injury occured
            longest_run: --int: The users longest average weekly long run
            goal_date: --string: The date of the users most important race
            pace_estimates: --list: The users pace estimates (in sec/mile) for each distance: please just type it out using the defined variables above. 
                Also initialize all your lists to -1 so we can check if they are set.
            available_dats: --list: The days of the week the user can run in the form of:
                                    0 - unavailable
                                    1 - available
                                    2 - long run
            number_of_days: --int: The number of days a user wants to run per week
            user_id: --int The user's id
            workout_RPE: --dict: Users mean RPE for each type of run
        """
        #training storage
        storage = storage_stacks_and_queues()
        #inputs
        self.dob = dob
        self.sex = sex
        self.running_ex = running_ex
        self.injury = injury
        self.most_recent_injury = most_recent_injury
        self.longest_run = longest_run
        self.goal_date = goal_date
        self.pace_estimates = pace_estimates
        self.available_days = available_days
        self.number_of_days = number_of_days
        self.user_id = user_id
        self.workout_RPE = workout_RPE
        #workout storage
        self.month_history = storage.month_history
        self.week_history = storage.week_history
        self.day_history = storage.day_history
        self.month_future = storage.month_future
        self.week_future = storage.week_future
        self.day_future = storage.day_future
        #additional information
        self.age = self.get_age()


        

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
            type, (new_mean, (info[DAYS]+1), new_deviation))  # Update the information

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

    
    def user_id_exists(user_id: int) -> bool:
        """" Checks if a user_id exists in the database."""
        
        conn = init_db()
        curr = conn.cursor()
        
        try:
            # Check if the user_id exists in the user_credentials table
            query = """
                SELECT 1 FROM public.user_credentials WHERE user_id = %s;
            """
            curr.execute(query, (user_id,))
            exists = curr.fetchone()
            return bool(exists)

        finally:
            # Close the cursor and connection
            curr.close()
            conn.close() 
            
            
    def generate_new_id(self) -> None:
        """ Generates a new user ID for the user.
        This function generates a new user ID that is not already in use by checking the database."""
        
        # Generate a new user ID
        new_user_id = secrets.randbelow(900000000) + 10000000
        
        # Check if the user ID already exists in the database
        if (user.user_id_exists(new_user_id)):
            logging.warning("User ID already exists, generating a new one.")
            self.generate_new_id() 
        
        self.user_id = new_user_id
        

    def get_age(self) -> int:
        """Returns the number of years the user has been alive as an int"""
        today = datetime.date.today()
        dob = datetime.datetime.strptime(self.dob, "%Y-%m-%d").date()
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

    def get_training_pace(self, workout_type) -> int:
        """Returns the training pace for a given type of workout based on the users 5k prediction time."""
        if self.pace_estimates[FIVEK] == -1:
            raise ValueError("5k prediction time is not assigned.")
            
        if workout_type == EASY:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 0.65)
        elif workout_type == PROGRESSION:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 0.82)
        elif workout_type == RECOVERY:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 0.62)
        elif workout_type == THRESHOLD:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 0.87)
        elif workout_type == LONGRUN:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 0.7)
        elif workout_type == VO2MAX:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 0.95)
        elif workout_type == TEMPO:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 0.82)
        else:
            return 0
        
    def txt_to_workout_type(txt: str) -> int:
        """Converts a string to the corresponding workout type index."""
        workout_types = {
            "Three K": THREEK,
            "Five K": FIVEK,
            "Ten K": TENK,
            "Recovery Run": RECOVERY,
            "Easy Run": EASY,
            "Tempo Run": TEMPO,
            "Progression Run": PROGRESSION,
            "Threshold Run": THRESHOLD,
            "Long Run": LONGRUN,
            "VO2 Max Run": VO2MAX
        }
        return workout_types.get(txt, -1)
        
    

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