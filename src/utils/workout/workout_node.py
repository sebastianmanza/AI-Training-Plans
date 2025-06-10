# Basic definition of a node for a tree
class workout_node:
    _slots_ = ("depth", "reps", "set", "pace", "unit")

    def __init__(self, reps: int, set: str, pace: int, unit: bool):
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


test_workout = workout_node(3, None, None, False)
times_two = workout_node(2, None, None, False)
four_by_one = workout_node(4, 100, "7:30", False)  # 4x100 at 7:30
four_by_two = workout_node(4, 200, "8:00", False)  # 4x200 at 8:00
test_workout.add(times_two)
test_workout.add(times_two)
times_two.add(four_by_one, four_by_two)

mile_workout = workout_node(None, 2, "ET", True)

print(str(test_workout))
print(str(mile_workout))
