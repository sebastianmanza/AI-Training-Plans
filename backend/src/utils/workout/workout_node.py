# Basic definition of a node for a tree
import copy


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
            new_node = copy.copy(node)
            new_node.depth = self.depth+1
            self.children.append(new_node)

    def __str__(self):
        return self.str_helper(0)

    # A simple to string
    def str_helper(self, depth: int):
        toReturn = "   "*depth
        if (self.reps != None and self.reps != 1):
            toReturn += f"{self.reps}x"
        if (self.set != None):
            toReturn += f"{self.set}"
        if self.unit:
            toReturn += " mile(s)"
        if (self.pace != None):
            toReturn += f" at {self.pace}"
        toReturn += '\n'
        depth += 1
        for child in self.children:
            toReturn += child.str_helper(depth)
        return toReturn

    # A way of calculating mileage based on the meters run in a workout
    def mileage(self):
        return int(self.meterage())/METERS_PER_MILE

    # A way of calculating the meters run in a workout
    def meterage(self):
        multiplier = self.reps
        if (self.set != None):
            if self.unit:
                multiplier *= METERS_PER_MILE
            return multiplier * (int(self.set))
        else:
            total = 0
            for child in range(len(self.children)):
                total += multiplier * self.children[child].meterage()
            return total

    # Alter the number of reps ("" alters the root node, "0" alters the node below it)
    def alter_reps(self, num_change: int, child_path: str):
        if (child_path != ""):
            path = int(child_path[0])
            self.children[path].alter_reps(
                num_change, (child_path[1:]))
        else:
            self.reps += num_change

    # Alter the number of reps ("" alters the root node, "0" alters the node below it)
    def alter_sets(self, num_change: int, child_path: str):
        if (child_path != ""):
            path = int(child_path[0])
            self.children[path].alter_sets(
                num_change, (child_path[1:]))
        else:
            self.set += num_change


# Test code (feel free to mess around/delete)
test_workout = workout_node(None, 4, None, None, False)
times_two = workout_node(None, 4, None, None, False)
four_by_one = workout_node(None, 1, 100, "7:30", False)  # 4x100 at 7:30
four_by_two = workout_node(None, 4, 100, "8:00", False)  # 4x200 at 8:00
test_workout.add(times_two)
test_workout.add(times_two)
test_workout.add(four_by_one)
times_two.add(four_by_one, four_by_two)
# print(test_workout)

mile_workout = workout_node("ET", 1, 2, "ET", True)
# print(test_workout)


test_workout.alter_reps(12, "2")
print(test_workout)
