from collections import deque
from queue import Queue

class storage_stacks_and_queues:
    # stores history of trainging for months, weeks, and days in a stack
    month_stack = deque()
    week_stack = deque()
    day_stack = deque()

    # stores predicted future training for months, weeks, and days in a queue
    month_queue = Queue()
    week_queue = Queue()
    day_queue = Queue()

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