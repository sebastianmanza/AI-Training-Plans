import backend.src.utils.user_storage.day_plan as day_plan
import backend.src.utils.user_storage.month_plan as month_plan
import backend.src.utils.user_storage.week_plan as week_plan
from backend.src.utils.user_storage.storage_stacks_and_queues import *

class training_database:
    
    # create static instance
    storage = storage_stacks_and_queues()
    
    def __init__(self, day: day_plan, week: week_plan, month: month_plan):
        
        self.day = training_database.storage.day_future
        self.week = training_database.storage.week_future
        self.month = training_database.storage.month_future


