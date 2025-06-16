import psycopg2
from backend.src.utils.SQLutils.database_connect import db_select
from backend.src.utils.user_storage.user import user
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.user_storage.month_plan import month_plan
from backend.src.utils.user_storage.week_plan import week_plan
from backend.src.utils.user_storage.day_plan import day_plan

class UserNotFoundError(Exception):
    """Exception raised when a user is not found in the database. """
    def __init__(self, user_id):
        super().__init__(f"No user found with ID {user_id}.")


def retrieve_user_info(user_id: int, username, pwd, col_names = False) -> user:
    """
    Retrieves user information from the database and populates it in a user object.
    
    Args:
        user_id (int): The ID of the user to retrieve.
        username (str): The username for database connection.
        pwd (str): The password for database connection.
    
    Returns:
        user: An instance of the user class containing user details.
    """
    
    # Prepare the queries
    user_query = """
        SELECT userid, dob, sex, runningex, fivekm, goaldate, mean_rpe, std_rpe
        FROM userlistai
        WHERE userid = %s;
        """
    
    month_query = """
        SELECT total_mileage AS month_total_mileage, goal_stimuli AS month_goal_stimuli, cycle AS month_cycle, expected_rpe AS month_expected_rpe, 
               complete_mileage AS month_completed_mileage, complete_score AS month_percent_completion, 
               real_rpe AS month_real_rpe, month_id, past_month
        FROM month_cycle
        WHERE user_id = %s;
    """
    
    week_query = """
        SELECT total_mileage AS week_total_mileage, goal_stimuli AS week_goal_stimuli, cycle AS week_cycle, expected_rpe AS week_expected_rpe, 
               complete_mileage AS week_completed_mileage, complete_score AS week_percent_completion, 
               real_rpe AS week_real_rpe, week_id, past_week
        FROM week_cycle
        WHERE user_id = %s;
    """
    
    day_query = """
        SELECT total_mileage AS day_total_mileage, goal_stimuli AS day_goal_stimuli, cycle AS day_cycle, expected_rpe AS day_expected_rpe,
                complete_mileage AS day_completed_mileage, complete_score AS day_percent_completion, 
                real_rpe AS day_real_rpe, past_day
        FROM day_cycle
        WHERE user_id = %s;
    """
    
    
    # Execute queries
    if col_names:
        user_info, user_cursor = db_select(username, pwd, user_id, user_query, return_cursor=True)
        month_info, month_cursor = db_select(username, pwd, user_id, month_query, return_cursor=True)
        week_info, week_cursor = db_select(username, pwd, user_id, week_query, return_cursor=True)
        day_info, day_cursor = db_select(username, pwd, user_id, day_query, return_cursor=True)
        
        # Retrieve column names
        user_columns = [desc[0] for desc in user_cursor.description]
        month_columns = [desc[0] for desc in month_cursor.description]
        week_columns = [desc[0] for desc in week_cursor.description]
        day_columns = [desc[0] for desc in day_cursor.description]
        
        return {
            "user_info": (user_columns, user_info),
            "months": (month_columns, month_info),
            "weeks": (week_columns, week_info),
            "days": (day_columns, day_info)
        }
    
    user_info = db_select(username, pwd, user_id, user_query)
    month_info = db_select(username, pwd, user_id, month_query)
    week_info = db_select(username, pwd, user_id, week_query)
    day_info = db_select(username, pwd, user_id, day_query)
    
    return {
        "user_info": user_info,
        "months": month_info,
        "weeks": week_info,
        "days": day_info
    }

def create_data_dicts(data, columns):
    """
    Creates a list of dictionaries mapping column names to their values for each row in the data.

    Args:
        data (list): List of rows containing data.
        columns (list): List of column names.

    Returns:
        list: List of dictionaries for each row in the data.
    """
    if not data:
        return {}
    
    return [
        {col: row[i] if i < len(row) else None for i, col in enumerate(columns)}
        for row in data
    ]
    
def populate_user_info(user_id) -> user:
    """
    Populates user information from the database into a user object.
    
    Args:
        user_id (int): The ID of the user to retrieve.
    
    Returns:
        user: An instance of the user class populated with user details.
    """
    # Retrieve user information
    user_info = retrieve_user_info(user_id, DB_CREDENTIALS["username"], DB_CREDENTIALS["password"], True)
    
    if not user_info:
        raise UserNotFoundError(user_id)
    
    # Extract column names and data
    user_data = user_info['user_info'][1]
    user_columns = user_info['user_info'][0]
    month_data = user_info['months'][1]
    month_columns = user_info['months'][0]
    week_data = user_info['weeks'][1]
    week_columns = user_info['weeks'][0]
    day_data = user_info['days'][1]
    day_columns = user_info['days'][0]
    
    print("User Info:", user_info)
    print("User Data:", user_data)
    print("User Columns:", user_columns)
    
    # Create a dictionary mapping column names to their values
    user_data_dict = create_data_dicts(user_data, user_columns)
    month_data_dicts = create_data_dicts(month_data, month_columns)
    week_data_dicts = create_data_dicts(week_data, week_columns)
    day_data_dicts = create_data_dicts(day_data, day_columns)
    
    
    # Create a new user object
    new_user = user(
        user_id = user_data_dict[0].get('userid'),
        age = user_data_dict[0].get('dob'),
        sex = user_data_dict[0].get('sex'),
        running_ex = user_data_dict[0].get('runningex'),
        five_km_estimate = user_data_dict[0].get('fivekm'),
        goal_date = user_data_dict[0].get('goaldate'),
        mean_RPE = user_data_dict[0].get('mean_rpe'),
        STD_RPE = user_data_dict[0].get('std_rpe')
    )
    
    # Populate the months objects
    for month_data_dict in month_data_dicts:
        if (month_data_dict.get('past_month')):
            new_user.month_history.append(month_plan(
            total_mileage = month_data_dict.get('month_total_mileage'),
            goal_stimuli = month_data_dict.get('month_goal_stimuli'),
            cycle = month_data_dict.get('month_cycle'),
            expected_rpe = month_data_dict.get('month_expected_rpe'),
            real_rpe = month_data_dict.get('month_real_rpe'),
            complete_score = month_data_dict.get('month_percent_completion'),
            month_id = month_data_dict.get('month_id')
        ))
        else:
            new_user.month_future.put(month_plan(
            total_mileage = month_data_dict.get('month_total_mileage'),
            goal_stimuli = month_data_dict.get('month_goal_stimuli'),
            cycle = month_data_dict.get('month_cycle'), 
            expected_rpe = month_data_dict.get('month_expected_rpe'),
            month_id = month_data_dict.get('month_id')))

    # Populate the weeks objects
    for week_data_dict in week_data_dicts:
        if (week_data_dict.get('past_week')):
            new_user.week_history.append(week_plan(
            total_mileage = week_data_dict.get('week_total_mileage'),
            goal_stimuli = week_data_dict.get('week_goal_stimuli'),
            cycle = week_data_dict.get('week_cycle'),
            expected_rpe = week_data_dict.get('week_expected_rpe'),
            real_rpe = week_data_dict.get('week_real_rpe'),
            complete_score = week_data_dict.get('week_percent_completion'),
            week_id = week_data_dict.get('week_id')
        ))
        else:
            new_user.week_future.put(week_plan(
            total_mileage = week_data_dict.get('week_total_mileage'),
            goal_stimuli = week_data_dict.get('week_goal_stimuli'),
            cycle = week_data_dict.get('week_cycle'), 
            expected_rpe = week_data_dict.get('week_expected_rpe'),
            week_id = week_data_dict.get('week_id')))

    
    # Populate the days objects
    # Populate the weeks objects
    for day_data_dict in day_data_dicts:
        if (day_data_dict.get('past_day')):
            new_user.day_history.append(day_plan(
            total_mileage = day_data_dict.get('day_total_mileage'),
            goal_stimuli = day_data_dict.get('day_goal_stimuli'),
            cycle = day_data_dict.get('day_cycle'),
            expected_rpe = day_data_dict.get('day_expected_rpe'),
            real_rpe = day_data_dict.get('day_real_rpe'),
            complete_score = day_data_dict.get('day_percent_completion'),
            day_id = day_data_dict.get('day_id')
        ))
        else:
            new_user.day_future.put(day_plan(
            total_mileage = day_data_dict.get('day_total_mileage'),
            goal_stimuli = day_data_dict.get('day_goal_stimuli'),
            cycle = day_data_dict.get('day_cycle'), 
            expected_rpe = day_data_dict.get('day_expected_rpe'),
            day_id = day_data_dict.get('day_id')))
    
    
    return new_user
# Testing
print(populate_user_info(1).age) 

# Column names: 'userid', 'dob', 'sex', 'runningex', 'fivekm', 'goaldate', 'mean_rpe', 'std_rpe', 'user_id', 'total_mileage', 'goal_stimuli', 'cycle', 'expected_rpe', 'real_rpe', 'complete_score', 'month_id', 'month_id', 'total_mileage', 'goal_stimuli', 'cycle', 'expected_rpe', 'real_rpe', 'complete_score', 'week_id', 'week_id', 'total_mileage', 'goal_stimuli', 'cycle', 'expected_rpe', 'real_rpe', 'complete_score'