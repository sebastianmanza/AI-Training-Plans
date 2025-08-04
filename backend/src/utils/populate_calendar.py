import calendar
from backend.scripts.txt_to_database import txt_to_database  # pragma: no cover
from backend.src.utils.SQLutils.database_connect import init_db, db_select  # pragma: no cover
from backend.src.utils.SQLutils.user_retrieve import convert_trio_types_to_tuples, populate_user_info  # pragma: no cover
from backend.src.utils.SQLutils.user_send import cast_workouts_to_trios, send_user_all, send_user_creds  # pragma: no cover
from backend.src.utils.user_storage.user import user  # pragma: no cover
from backend.src.utils.SQLutils.config import DB_CREDENTIALS  # pragma: no cover
from psycopg2.extras import register_composite  # pragma: no cover
from datetime import datetime
import queue
import copy
from datetime import timedelta


def clone_queue(origin_queue):
    """
    Safley clones queue to avoid permanent removal of original static queue.
    """
    temp_list = []

    while not origin_queue.empty():
        temp_list.append(origin_queue.get())

    cloned_queue = queue.Queue()

    for item in temp_list:
        origin_queue.put(item)
        try:
            cloned_queue.put_nowait(copy.deepcopy(item))
        except queue.Full:
            raise RuntimeError("Cloned queue overflowed unexpectedly")

    return cloned_queue


def month_list(in_session_user):
    """Returns a list of months as strings to dependant on the number of month objects found with
    the in-session user.
    """
    
    curr_month_index = datetime.now().month
    curr_year_index = datetime.now().year
    month_names = []
    num_months = in_session_user.month_future.qsize() + len(in_session_user.month_history)
    
    for i in range(num_months):
        # Calculate the month index and year
        month_index = (curr_month_index - 1 + i) % 12 + 1
        year_adjustment = (curr_month_index - 1 + i) // 12
        year = curr_year_index + year_adjustment
        # Get the month name and append it to the list
        month_name = f"{calendar.month_name[month_index]}"
        month_names.append((month_name, year))
        

    return month_names
   
    
def fill_day_data(in_session_user):
    """ 
    Returns a list of touples of day objects and their assigned date based off the users start point.
    """
    
    # Clone the day future queue to avoid modifying the original
    cloned_day_queue = clone_queue(in_session_user.day_future)
    
    list_of_tuple_days = []
    current_date = datetime.now()
    
    # First iterate through past training sessions
    for day in in_session_user.day_history:
        # Attach an absolute date to the day
        list_of_tuple_days.append((day, current_date))
        current_date += timedelta(days=1)
    
    # Assign the dates to future training sessions util the queue is empty
    while not cloned_day_queue.empty():
        
        day = cloned_day_queue.get()
        # Attach an absolute date to the day
        list_of_tuple_days.append((day, current_date))
        current_date += timedelta(days=1)
    
    return list_of_tuple_days


def month_name_to_index(month_name):
    """
    Converts a month name to its corresponding index (1-12).
    """
    date = datetime.strptime(month_name, "%B")
    return date.month


def month_day_list(month_names, list_of_tuple_days):
    """
    Attaches days to month list for ease of front end translation.
    """
    
    # list of tuples to hold month name and its corresponding days
    month_day_list = []
    for i in range(len(month_names)):
        curr_month = month_names[i][0]
        year = month_names[i][1]
        
        # day counter
        j = 0
        # Find the index of the first day that belongs to the current month
        while month_name_to_index(curr_month) == list_of_tuple_days[i][1].month and j < len(list_of_tuple_days):
             # Initialize a temporary list to hold days for the current month
            temp_lst = []
            temp_lst.append(list_of_tuple_days[j][0])
            j += 1
        
        # Append the month name, year, and the list of days to the month_day_lis
        month_day_list.append((year, curr_month, temp_lst))  
        
    return month_day_list

    
test_user = user(dob="2005-03-17", sex="Male", running_ex="Advanced", injury=0, most_recent_injury=0,
                 longest_run=12, goal_date="2026-01-01", available_days=[1, 1, 0, 1, 1, 2, 1], number_of_days=7,
                 pace_estimates=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
database = txt_to_database("backend/data/raw/training_plan_test.txt")
test_user.day_future = database.day
test_user.week_future = database.week
test_user.month_future = database.month   

month_names = month_list(test_user)
list_of_tuple_days = fill_day_data(test_user)


print(month_names)

print(month_day_list(month_names, list_of_tuple_days))


