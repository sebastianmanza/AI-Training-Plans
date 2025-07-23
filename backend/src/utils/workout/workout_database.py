from backend.src.utils.workout.workout_storage import workout_storage
from backend.src.utils.workout.single_workout import single_workout, TRIO_STIM, TRIO_RPE, TRIO_DIST


LARGE_NUM = 4000


class workout_database:

    storage = workout_storage()

    # Creates a trio that can be used as a key in the workout dictionary.
    @staticmethod
    def create_trio(stim, rpe, dist) -> tuple:
        stim, rpe, dist = float(stim), float(rpe), float(dist)
        return (stim, rpe, dist)

    # x range is 1 - 7 stimulus, y range is 1 -10 RPE, z range is 1 - 10 Distance
    # Dictionary that maps trios of (x, y, z) coordinates to workout types.
    workout_dictionary = {
        create_trio.__func__(2.5, 4, 5.5): "Easy Run",
        create_trio.__func__(2, 3, 4.5): "Recovery Run",
        create_trio.__func__(4, 6, 6): "Progression",
        create_trio.__func__(2.5, 5, 10): "Long Run",
        create_trio.__func__(4.5, 7, 7.5): "Threshold",
        create_trio.__func__(5, 6, 7): "Fartlek",
        create_trio.__func__(5.5, 8, 6.5): "Race Pace Interval",
        create_trio.__func__(6.5, 2, .5): "Strides",
        create_trio.__func__(7, 3, .5): "Hill Sprints",
        create_trio.__func__(7, 6, .5): "Flat Sprints",
        create_trio.__func__(6, 10, 3): "Time Trial",
        create_trio.__func__(1, 2, 3): "Warmup and Cooldown",
        create_trio.__func__(0, 0, 0,): "Off"
    }

    def __init__(self, easyrun: list = [], recovery: list = [], kenyan: list = [],
                 long: list = [], threshold: list = [], fartlek: list = [],
                 race_pace_interval: list = [], strides: list = [], hill_sprints: list = [],
                 flat_sprints: list = [], time_trial: list = [], warmup_and_cooldown: list = []):

        # Set up the collection of workouts of each type
        self.easyrun = workout_database.storage.easyrun
        self.recovery = workout_database.storage.recovery
        self.kenyan = workout_database.storage.kenyan
        self.long = workout_database.storage.long
        self.threshold = workout_database.storage.threshold
        self.fartlek = workout_database.storage.fartlek
        self.race_pace_interval = workout_database.storage.race_pace_interval
        self.strides = workout_database.storage.strides
        self.hill_sprints = workout_database.storage.hill_sprints
        self.flat_sprints = workout_database.storage.flat_sprints
        self.time_trial = workout_database.storage.time_trial
        self.warmup_and_cooldown = workout_database.storage.warmup_and_cooldown

    # This function is finicky but a god send. Make sure to reference it when you would write if/else statements
    def match_execute(self, workout_type: str, func, *args):
        """Match the workout type to the corresponding list and execute the function with args"""
        match workout_type:
            case "Easy Run":
                return func(self.easyrun, *args)
            case "Recovery Run":
                return func(self.recovery, *args)
            case "Progression":
                return func(self.kenyan, *args)
            case "Long Run":
                return func(self.long, *args)
            case "Threshold":
                return func(self.threshold, *args)
            case "Fartlek":
                return func(self.fartlek, *args)
            case "Race Pace Interval":
                return func(self.race_pace_interval, *args)
            case "Strides":
                return func(self.strides, *args)
            case "Hill Sprints":
                return func(self.hill_sprints, *args)
            case "Flat Sprints":
                return func(self.flat_sprints, *args)
            case "Time Trial":
                return func(self.time_trial, *args)
            case _:  # Default case for Warmup and Cooldown
                return func(self.warmup_and_cooldown, *args)

    def add_workout(self, workout: single_workout) -> None:
        """Add a workout to the matching workout database"""
        self.match_execute(workout_database.get_workout_type(workout.get_stim(), workout.get_rpe(), workout.get_distance()),
                           list.append, workout)

    def mass_add_workouts(self, workouts) -> None:
        """"Add a list of workouts to the database"""
        for workout in workouts:
            self.add_workout(workout)
            # try:
            #     self.add_workout(workout)
            # except TypeError:  # If the workout isn't a single_workout instance, raise an error
            #     print(TypeError)

    def print_all_type(self, type_list: list, workout_type: str) -> None:
        """Print out all workouts of a specific type"""
        print(f"{workout_type} Workouts:")
        for workout in type_list:
            print(workout)

    def print_workouts(self, workout_type: str) -> None:
        """Print out every workout of an inputted type"""
        self.match_execute(workout_type, self.print_all_type, workout_type)

    # Returns a workout type based on the given x,y and z coordinates represented as stim, rpe and dist.
    @staticmethod
    def get_workout_type(stim: float, rpe: float, dist: float) -> str:
        """Returns the workout type based on stim, rpe, and dist"""
        distance, final_trio = LARGE_NUM, workout_database.create_trio(
            0, 0, 0)  # Set initial values
        for trio in workout_database.workout_dictionary:
            new_distance = workout_database.get_distance(trio, stim, rpe, dist)
            if new_distance < distance:
                distance, final_trio = new_distance, trio  # Update the closest workout type

        # If the distance isn't 0 then a workout type hasn't been found.
        if final_trio == (0, 0, 0) and not dist == 0:
            raise ValueError(
                "No matching workout type found for the given coordinates.")
        return workout_database.workout_dictionary[final_trio]
    
    def equalTrio(trio, other_trio):
        """Check if two trios are equal"""
        return trio[TRIO_STIM] == other_trio[TRIO_STIM] and trio[TRIO_RPE] == other_trio[TRIO_RPE] and trio[TRIO_DIST] == other_trio[TRIO_DIST]

    @staticmethod
    def get_workout_type_trio(trio: tuple) -> str:
        """Returns the workout type based on the trio"""
        # Similar to a get_workout_type but with different input
        print(trio)
        stim = float(trio[TRIO_STIM])
        rpe = float(trio[TRIO_RPE])
        dist = float(trio[TRIO_DIST])
        return workout_database.get_workout_type(stim, rpe, dist)

    def get_workout_storage_type(self, workout_type: str) -> list:
        """Returns the list of workouts of a specific type"""
        return self.match_execute(workout_type, lambda lst: lst)  # Identity lambda function.

    def get_individual_workout_helper(self, stim: float, rpe: float, dist: float, workout_type: str) -> single_workout:
        """Returns the workout closest to the stim,rpe and dist from within the type"""
        distance, final_workout = LARGE_NUM, self.get_workout_storage_type(
            workout_type)[0]  # Set inital values that work as a default
        # Search throught the workouts of this type
        for workout in self.get_workout_storage_type(workout_type):
            new_distance = workout_database.get_distance(
                workout.get_trio(), stim, dist, rpe)  # Find the distance
            if new_distance < distance:  # Adjust values
                distance, final_workout = new_distance, workout

        return final_workout

    def get_individual_workout(self, stim: float, rpe: float, dist: float) -> single_workout:
        workout_type = self.get_workout_type(
            stim, rpe, dist)  # Get the workout type based on the trio
        # Find the closest workout within the particular database
        return self.get_individual_workout_helper(stim, rpe, dist, workout_type)

    def get_workout_type_coordinates(self, stim: float, rpe: float, dist: float) -> tuple:
        """Given stim, rpe, and dist return the coordinates associated with the workout type"""
        if dist == 0:  # If the distance is 0 then return the off workout
            return workout_database.create_trio(0, 0, 0)
        final_trio, distance = workout_database.create_trio(
            0, 0, 0), LARGE_NUM  # Inital values
        for trio in workout_database.workout_dictionary:
            new_distance = workout_database.get_distance(trio, stim, rpe, dist)
            if new_distance < distance:  # If the workout is closer set it as the closest workout
                distance, final_trio = new_distance, trio

        # Check to see that a workout was found
        if not final_trio == (0, 0, 0):
            return final_trio
        # If no workout was found then raise an error
        raise ValueError(
            "No matching workout type found for the given coordinates.")

    def get_workout_difference(stim: float, rpe: float, dist: float) -> tuple:
        """Return the difference between the inputted stim, rpe, and dist and the workout type it is associated with"""
        workout_trio = workout_database.get_workout_type_coordinates(
            stim, rpe, dist)
        return workout_database.create_trio(
            (stim - workout_trio[TRIO_STIM]),
            (rpe - workout_trio[TRIO_RPE]),
            (dist - workout_trio[TRIO_DIST]))

    def get_distance(trio: tuple, stim: float, rpe: float, dist: float) -> float:
        return (trio[TRIO_STIM] - stim) ** 2 + (trio[TRIO_RPE] - rpe) ** 2 + (trio[TRIO_DIST] - dist) ** 2
