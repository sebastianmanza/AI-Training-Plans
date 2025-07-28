# import training
import logging
import math
import secrets
import datetime
from backend.src.utils.user_storage.storage_stacks_and_queues import storage_stacks_and_queues
import backend.src.utils.user_storage.training_database as training_database
from backend.src.utils.SQLutils.database_connect import init_db
from backend.src.utils.pace_calculations import get_training_pace_helper, to_str, mile_pace
from backend.src.utils.SQLutils.config import DB_CREDENTIALS

FIVEKDIST, METERS_PER_MILE = 5000, 1600  # Distance conversions
CALCNUM = 1.06  # Exponent for pace prediction
RPE, DAYS, DEVIATION = 0, 1, 2  # Indexes used for mean RPE
DEFAULT_WORKOUT_NUMS = {  # Associate each workout type with a number of days (used in future calculations) average RPE and standard deciation
    "Easy Run": (0, 0, 0), "Recovery Run": (0, 0, 0), "Progression": (0, 0, 0), "Long Run": (0, 0, 0),
    "Threshold": (0, 0, 0), "Fartlek": (0, 0, 0), "Race Pace Interval": (0, 0, 0), "Strides": (0, 0, 0),
    "Hill Sprints": (0, 0, 0), "Flat Sprints": (0, 0, 0), "Time Trial": (0, 0, 0), "Warmup and Cooldown": (0, 0, 0), "Off": (0, 0, 0)}

THREEK, FIVEK, TENK, RECOVERY, EASY, TEMPO, PROGRESSION, THRESHOLD, LONGRUN, VO2MAX = range(
    10)


class user:
    # __slots__ = ("dob", "sex", "running_ex", "injury", "most_recent_injury", "longest_run", "goal_date", "pace_estimates", "available_days", "number_of_days", "user_id", "workout_RPE")

    def __init__(self, dob: str, sex: str, running_ex: str, injury: int, most_recent_injury: int, longest_run: int,  goal_date: str,
                 available_days: list, number_of_days: int, pace_estimates: list = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], user_id: int = secrets.randbelow(90000000) + 10000000, workout_RPE=DEFAULT_WORKOUT_NUMS):
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
        # training storage
        storage = storage_stacks_and_queues()
        # inputs
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
        # workout storage
        self.month_history = storage.month_history
        self.week_history = storage.week_history
        self.day_history = storage.day_history
        self.month_future = storage.month_future
        self.week_future = storage.week_future
        self.day_future = storage.day_future
        # additional information
        self.age = self.get_age()

    # Update the mean_RPE using the workout type and the RPE

    def update_mean_RPE(self, type: str, given_RPE: float, expected_RPE: float) -> None:
        """Update the values associated with a given workout type"""
        info = self.workout_RPE.get(type)  # Get the info for the workout type
        new_mean = ((info[RPE]*info[DAYS]) + given_RPE) / \
            (info[DAYS]+1)  # Calculate the new mean
        # Calculate the new average deviation
        new_deviation = ((info[DEVIATION]*info[DAYS]) +
                         abs(given_RPE-expected_RPE)) / (info[DAYS]+1)
        self.workout_RPE.update(
            # Update the information
            type, (new_mean, (info[DAYS]+1), new_deviation))

    def get_type_mean_RPE(self, type: str) -> float:
        """Returns the mean RPE for a given workout type"""
        return self.workout_RPE[type][RPE]

    def get_type_deviation_RPE(self, type: str) -> float:
        """Returns the deviation of the RPE for a given workout type"""
        return self.workout_RPE[type][DEVIATION]

    def set_5k_pace(self, new_pace) -> None:
        """Set the pace for a distance in seconds. This updates the pace"""
        if isinstance(new_pace, str):
            self.pace_estimates[FIVEK] = mile_pace(new_pace, 5000)
        else:
            self.pace_estimates[FIVEK] = new_pace

    def get_pace(self, distance: int) -> int:
        """Returns the pace for a distance in seconds"""
        return self.pace_estimates[distance]

    # Makes the predictions for every distance in DISTANCES.
    def make_predictions(self) -> None:
        """"""
        for distance in range(self.pace_estimates.__len__()):
            self.pace_estimates[distance] = self.get_training_pace(distance)

    # Returns the mile pace for each distance.

    def get_times(self) -> str:
        toReturn = ""
        for pace in self.pace_estimates:
            toReturn += f"{to_str(pace)}\n"
        return toReturn

    def get_user_id(self) -> int:
        return self.user_id

    def user_id_exists(user_id: int) -> bool:
        """" Checks if a user_id exists in the database."""

        conn = init_db(DB_CREDENTIALS["DB_USERNAME"],
                       DB_CREDENTIALS["DB_PASSWORD"])
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

    def generate_new_id() -> int:
        """ Generates a new user ID for the user.
        This function generates a new user ID that is not already in use by checking the database."""

        # Generate a new user ID
        new_user_id = secrets.randbelow(90000000) + 10000000

        # Check if the user ID already exists in the database
        if (user.user_id_exists(new_user_id)):
            logging.warning("User ID already exists, generating a new one.")
            user.generate_new_id()

        return new_user_id

    def get_age(self) -> int:
        """Returns the number of years the user has been alive as an int"""
        today = datetime.date.today()
        dob = datetime.datetime.strptime(self.dob, "%Y-%m-%d").date()
        age = today.year - dob.year - \
            ((today.month, today.day) < (dob.month, dob.day)
             )  # Adjust for whether the birthday has occurred this year
        return age

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
    def modify_pace(self, change: int, distance: int) -> int:
        return self.pace_estimates[distance] + change

    def get_training_pace(self, workout_type: int) -> int:
        """Returns the training pace for a given type of workout based on the users 5k prediction time."""
        if self.pace_estimates[FIVEK] == -1:
            raise ValueError("5k prediction time is not assigned.")

        if workout_type == FIVEK:
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

    def __eq__(self, other) -> bool:
        """Check if two user objects are equal based on their attributes."""
        if not isinstance(other, user):
            return False

        return (self.user_id == other.user_id and
                self.dob == other.dob and
                self.sex == other.sex and
                self.running_ex == other.running_ex and
                self.injury == other.injury and
                self.most_recent_injury == other.most_recent_injury and
                self.longest_run == other.longest_run and
                self.goal_date == other.goal_date and
                self.pace_estimates == other.pace_estimates and
                self.available_days == other.available_days and
                self.number_of_days == other.number_of_days)  # and
        # self.workout_RPE == other.workout_RPE) # Should add workoutRPE check and possibly storage

    def __repr__(self) -> str:
        return (
            f"user("
            f"user_id={self.user_id!r}, dob={self.dob!r}, sex={self.sex!r}, running_ex={self.running_ex!r},\n"
            f"     injury={self.injury!r}, most_recent_injury={self.most_recent_injury!r}, longest_run={self.longest_run!r},\n"
            f"     goal_date={self.goal_date!r}, age={self.age!r},\n"
            f"     pace_estimates={self.pace_estimates!r},\n"
            f"     available_days={self.available_days!r}, number_of_days={self.number_of_days!r},\n"
            f"     workout_RPE={self.workout_RPE!r},\n"
            f"     month_history={list(self.month_history)!r},\n"
            f"     week_history={list(self.week_history)!r},\n"
            f"     day_history={list(self.day_history)!r},\n"
            f"     month_future={list(self.month_future.queue)!r},\n"
            f"     week_future={list(self.week_future.queue)!r},\n"
            f"     day_future={list(self.day_future.queue)!r}\n"
            f"     workout_RPE={self.workout_RPE!r}"
            f")"
        )
