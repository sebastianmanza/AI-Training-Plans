# import training
from backend.src.utils.pace_calculations import get_training_pace_helper, to_str, mile_pace
import backend.src.utils.user_storage.training_database as training_database
from backend.src.utils.user_storage.storage_stacks_and_queues import storage_stacks_and_queues
import datetime
import secrets
import math
import logging
from typing import Optional

logger = logging.getLogger(__name__)

# Database utilities are optional during testing.  Import them lazily so that
# the module can be used without a full database stack available.  Tests that
# exercise database functionality can skip appropriately if these imports are
# missing.
try:  # pragma: no cover - simply providing a fallback
    from backend.src.utils.SQLutils.database_connect import init_db  # type: ignore
except Exception:  # ImportError, ModuleNotFoundError etc.
    init_db = None  # type: ignore

try:  # pragma: no cover - configuration may not exist in tests
    from backend.src.utils.SQLutils.config import DB_CREDENTIALS  # type: ignore
except Exception:  # pragma: no cover
    DB_CREDENTIALS = {}  # type: ignore

FIVEKDIST, METERS_PER_MILE = 5000, 1600  # Distance conversions
CALCNUM = 1.06  # Exponent for pace prediction
RPE, DAYS, DEVIATION = 0, 1, 2  # Indexes used for mean RPE
DEFAULT_WORKOUT_NUMS = {
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
        # ``dict.update`` expects a mapping, so pass a single-key dictionary
        # rather than separate key/value arguments.
        self.workout_RPE.update({
            type: (new_mean, (info[DAYS]+1), new_deviation)
        })

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
        """Return all predicted pace times as newline separated string."""
        toReturn = ""
        for pace in self.pace_estimates:
            toReturn += f"{to_str(pace)}\n"
        return toReturn

    def get_user_id(self) -> int:
        """Return the unique identifier for this user."""
        return self.user_id

    def user_id_exists(user_id: int) -> bool:
        """Checks if a ``user_id`` exists in the database."""

        if init_db is None or not DB_CREDENTIALS:
            raise RuntimeError("Database utilities are not configured")

        conn = init_db(DB_CREDENTIALS["DB_USERNAME"],
                       DB_CREDENTIALS["DB_PASSWORD"])
        if conn is None:
            # ``init_db`` returns ``None`` when the connection attempt fails.
            raise RuntimeError("Database utilities are not configured")

        try:
            curr = conn.cursor()
        except Exception as e:  # pragma: no cover - defensive safety net
            conn.close()
            raise RuntimeError("Database utilities are not configured") from e

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

    def generate_new_id() -> Optional[int]:
        """Generate a new user ID or ``None`` if uniqueness can't be verified."""

        new_user_id = secrets.randbelow(90000000) + 10000000

        if init_db is None or not DB_CREDENTIALS:
            logger.warning(
                "Database utilities unavailable; cannot ensure unique user ID.")
            return None

        try:
            if user.user_id_exists(new_user_id):
                logger.warning("User ID already exists, generating a new one.")
                return user.generate_new_id()
        except Exception as exc:  # RuntimeError or database errors
            logger.warning(
                "Could not verify user ID uniqueness; refusing to generate ID: %s",
                exc,
            )
            return None

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
        """Append a completed month to history."""
        self.month_history.append(month)

    def append_fut_month(self, month):
        """Queue a future month plan."""
        self.month_future.put(month)

    def append_week(self, week):
        """Append a completed week to history."""
        self.week_history.append(week)

    def append_fut_week(self, week):
        """Queue a future week plan."""
        self.week_future.put(week)

    def append_day(self, day):
        """Append a completed day to history."""
        self.day_history.append(day)

    def append_fut_day(self, day):
        """Queue a future day plan."""
        self.day_future.put(day)

        # Takes in a string and a user i.e. (5000+10, 17:30 5k runner) and returns the pace associated with it.

    def modify_pace(self, change: int, distance: int) -> int:
        """Adjust a stored pace value.

        Args:
            change (int): Number of seconds to add or subtract.
            distance (int): Index of the pace to modify.

        Returns:
            int: Updated pace in seconds.
        """
        return self.pace_estimates[distance] + change

    def get_training_pace(self, workout_type: int) -> int:
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
        elif workout_type == THREEK:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 1.05)
        elif workout_type == FIVEK:
            return self.pace_estimates[FIVEK]
        elif workout_type == TENK:
            return get_training_pace_helper(5000, self.pace_estimates[FIVEK] * 3.1, 0.97)
        else:
            return 0

    def txt_to_workout_type(txt: str) -> int:
        """Returns the corresponding integer (i.e THREEK or EASY) for a given workout type string.

        Args:
            txt (str): The input string in standard format ("Recovery Run")

        Returns:
            int: The corresponding integer for the workout type, or -1 if not found.
        """
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
        """Return a developer friendly representation of the user."""
        return (
            f"user("
            f"user_id={self.user_id!r}, dob={self.dob!r}, sex={self.sex!r}, running_ex={self.running_ex!r},\n"
            f"     injury={self.injury!r}, most_recent_injury={self.most_recent_injury!r}, longest_run={self.longest_run!r},\n"
            f"     goal_date={self.goal_date!r}, age={self.age!r},\n"
            f"     pace_estimates={self.pace_estimates!r},\n"
            f"     available_days={self.available_days!r}, number_of_days={self.number_of_days!r},\n"
            f"     workout_RPE={self.workout_RPE!r},\n"
            # f"     month_history={list(self.month_history)!r},\n"
            # f"     week_history={list(self.week_history)!r},\n"
            # f"     day_history={list(self.day_history)!r},\n"
            # f"     month_future={list(self.month_future.queue)!r},\n"
            # f"     week_future={list(self.week_future.queue)!r},\n"
            # f"     day_future={list(self.day_future.queue)!r}\n"
            f"     workout_RPE={self.workout_RPE!r}"
            f")"
        )
