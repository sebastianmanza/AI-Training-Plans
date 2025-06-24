import backend.src.utils.user_storage.day_plan as day_plan
import backend.src.utils.user_storage.month_plan as month_plan
import backend.src.utils.user_storage.week_plan as week_plan
from backend.src.utils.user_storage.storage_stacks_and_queues import storage_stacks_and_queues

class training_database:
    
    # create static instance
    storage = storage_stacks_and_queues()
    
    day = storage.day_future
    week = storage.week_future
    month = storage.month_future