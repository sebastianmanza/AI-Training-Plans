from collections import deque
from queue import Queue

class storage_stacks_and_queues:
    __slots__ = ("month_stack", "week_stack", "day_stack", "month_queue", "week_queue", "day_queue")

    # This class is used to store stacks and queues for month, week, and day
    def __init__(self):
        # Initialize the storage class
        self.month_stack = deque()
        self.week_stack = deque()
        self.day_stack = deque()

        self.month_queue = Queue()
        self.week_queue = Queue()
        self.day_queue = Queue()

# Example usage
# This code demonstrates how to use the storage class
storer = storage_stacks_and_queues
m_s = storer.month_stack
m_s.append("hi")
m_q = storer.month_queue
m_q.put("hello")
print(m_q.get())
print(m_s.pop())