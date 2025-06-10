# Basic definition of a node for a tree
class workout_node:
    _slots_ = ("depth", "reps", "set", "pace")

    def __init__(self, reps: int, set: int, pace: int):
        self.depth = 0
        self.reps = reps
        self.set = set
        self.pace = pace
        self.children = []

    def add(self, *nodes):
        for node in nodes:
            node.depth = self.depth+1
            self.children.append(node)

    def __str__(self):
        toReturn = "   "*self.depth
        toReturn += f"{self.reps}x"
        if (self.set != None):
            toReturn += f"{self.set} at {self.pace}"
        toReturn += '\n'
        for child in self.children:
            toReturn += str(child)
        return toReturn


test_workout = workout_node(3, None, None)
times_two = workout_node(2, None, None)
four_by_one = workout_node(4, 100, "7:30")  # 4x100 at 7:30
four_by_two = workout_node(4, 2, "8:00")  # 4x200 at 8:00
test_workout.add(times_two)
times_two.add(four_by_one, four_by_two)

print(str(test_workout))
