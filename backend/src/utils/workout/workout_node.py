# Basic definition of a node for a tree
class workout_node:
    global METERS_PER_MILE
    METERS_PER_MILE = 1600  # This approximation is used to calculate mileage
    _slots_ = ("workout_type", "depth", "reps", "set", "pace", "unit")

    def __init__(self, workout_type: str, reps: int, set: str, pace: str, unit: bool):
        self.workout_type = workout_type
        self.depth = 0
        self.reps = reps
        self.set = set
        self.pace = pace  # Pace i.e. 7:30 or ET
        self.children = []  # Sub-parts of the workout
        self.unit = unit  # True is miles, false is meters

    # Append any number of nodes to children, modifying their depth

    def add(self, *nodes):
        for node in nodes:
            node.depth = self.depth+1
            self.children.append(node)

    # A simple to string
    def __str__(self):
        toReturn = "   "*self.depth
        if (self.reps != None):
            toReturn += f"{self.reps}x"
        if (self.set != None):
            toReturn += f"{self.set}"
        if self.unit:
            toReturn += " mile(s)"
        if (self.pace != None):
            toReturn += f" at {self.pace}"
        toReturn += '\n'
        for child in self.children:
            toReturn += str(child)
        return toReturn

    # A way of calculating mileage based on the meters run in a workout
    def mileage(self):
        if not self.unit:
            return int(self.meterage())/METERS_PER_MILE
        else:
            return self.set

    # A way of calculating the meters run in a workout
    def meterage(self):
        multiplier = self.reps
        if (self.set != None):
            return multiplier * (int(self.set))
        else:
            total = 0
            for child in range(len(self.children)):
                total += multiplier * self.children[child].meterage()
            return total


# Test code (feel free to mess around/delete)
test_workout = workout_node(None, 4, None, None, False)
times_two = workout_node(None, 4, None, None, False)
four_by_one = workout_node(None, 1, 100, "7:30", False)  # 4x100 at 7:30
four_by_two = workout_node(None, 4, 100, "8:00", False)  # 4x200 at 8:00
test_workout.add(times_two)
test_workout.add(times_two)
times_two.add(four_by_one, four_by_two)
print(test_workout)

mile_workout = workout_node("ET", 1, 2, "ET", True)
print(mile_workout.mileage())
