from collections import deque
from queue import Queue


class storage_stacks_and_queues:
    """This class is used to store stacks and queues for month, week, and day"""

    __slots__ = ("month_history", "week_history", "day_history",
                 "month_future", "week_future", "day_future")

    def __init__(self):
        # Initialize the storage class
        # stacks
        self.month_history = deque()
        self.week_history = deque()
        self.day_history = deque()
        # queues
        self.month_future = Queue()
        self.week_future = Queue()
        self.day_future = Queue()


# Example usage
# This code demonstrates how to use the storage class
# storer = storage_stacks_and_queues()
# stacks info
# m_s = storer.month_history
# month = month_plan(100, "Endurance", "Base", 5)
# m_s.append(month)
# m_s.append("hi")
# m_s.append("there")
# m_s.append("how")
# m_s.append("are")
# m_s.append("you")
# i = 0
# while i < 4:
#    print(m_s.pop())
#    i += 1
# print(m_s.pop().goal_stimuli)  # Output: Endurance
# queues info
# m_q = storer.month_future
# m_q.put("hello")
# print(m_q.get())
