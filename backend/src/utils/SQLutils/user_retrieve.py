import psycopg2
from backend.src.utils.SQLutils.database_connect import db_select
from backend.src.utils.user_storage.user import user
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.user_storage.month_plan import month_plan
from backend.src.utils.user_storage.week_plan import week_plan
from backend.src.utils.user_storage.day_plan import day_plan

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
        SELECT user_id, sex, dob, runningex, fivekm, goaldate, mean_rpe, std_rpe
        FROM userlistai
        WHERE user_id = %s;
        """
    
    month_query = """
        SELECT total_mileage AS month_total_mileage, goal_stimuli AS month_goal_stimuli, cycle AS month_cycle, expected_rpe AS month_expected_rpe, 
               completed_mileage AS month_completed_mileage, percent_completion AS month_percent_completion, 
               real_rpe AS month_real_rpe, month_id, past_month
        FROM month_cycle
        WHERE user_id = %s;
    """
    
    week_query = """
        SELECT total_mileage AS week_total_mileage, goal_stimuli AS week_goal_stimuli, cycle AS week_cycle, expected_rpe AS week_expected_rpe, 
               completed_mileage AS week_completed_mileage, percent_completion AS week_percent_completion, 
               real_rpe AS week_real_rpe, week_id, past_week
        FROM week_cycle
        WHERE user_id = %s;
    """
    
    day_query = """
        SELECT total_mileage AS day_total_mileage, goal_stimuli AS day_goal_stimuli, cycle AS day_cycle, expected_rpe AS day_expected_rpe,
                completed_mileage AS day_completed_mileage, percent_completion AS day_percent_completion, 
                real_rpe AS day_real_rpe, day_id, past_day
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
    
    # Extract column names and data
    user_data = user_info['user_info'][1]
    user_columns = user_info['user_info'][0]
    month_data = user_info['months'][1]
    month_columns = user_info['months'][0]
    week_data = user_info['weeks'][1]
    week_columns = user_info['weeks'][0]
    day_data = user_info['days'][1]
    day_columns = user_info['days'][0]
    
    new_user = user(
        userid = user_data[0][user_columns.index('userid')],
        dob = user_data[0][user_columns.index('dob')],
        sex = user_data[0][user_columns.index('sex')],
        running_ex = user_data[0][user_columns.index('runningex')],
        five_km_estimate = user_data[0][user_columns.index('fivekm')],
        goal_date = user_data[0][user_columns.index('goaldate')],
        mean_RPE = user_data[0][user_columns.index('mean_rpe')],
        STD_RPE = user_data[0][user_columns.index('std_rpe')]
    )
    
    # Populate the months objects
    for month in month_data:
        if (month[month_columns.index('past_month')]):
            new_user.month_history.append(month_plan(
            total_mileage=month[month_columns.index('month_total_mileage')],
            goal_stimuli=month[month_columns.index('month_goal_stimuli')],
            cycle=month[month_columns.index('month_cycle')],
            expected_rpe=month[month_columns.index('month_expected_rpe')],
            real_rpe=month[month_columns.index('month_real_rpe')],
            complete_score=month[month_columns.index('month_percent_completion')],
            month_id=month[month_columns.index('month_id')]
        ))
        else:
            new_user.month_future.append(month_plan(
            total_mileage=month[month_columns.index('month_total_mileage')],
            goal_stimuli=month[month_columns.index('month_goal_stimuli')],
            cycle=month[month_columns.index('month_cycle')],
            expected_rpe=month[month_columns.index('month_expected_rpe')],
            month_id=month[month_columns.index('month_id')]))

    # Populate the weeks objects
    for week in week_data:
        if (week[week_columns.index('past_week')]):
            new_user.week_history.append(week_plan(
                total_mileage=week[week_columns.index('week_total_mileage')],
                goal_stimuli=week[week_columns.index('week_goal_stimuli')],
                cycle=week[week_columns.index('week_cycle')],
                expected_rpe=week[week_columns.index('week_expected_rpe')],
                real_rpe=week[week_columns.index('week_real_rpe')],
                complete_score=week[week_columns.index('week_percent_completion')],
                week_id=week[week_columns.index('week_id')]
            ))
        else:
            new_user.week_future.append(week_plan(
                total_mileage=week[week_columns.index('week_total_mileage')],
                goal_stimuli=week[week_columns.index('week_goal_stimuli')],
                cycle=week[week_columns.index('week_cycle')],
                expected_rpe=week[week_columns.index('week_expected_rpe')],
                week_id=week[week_columns.index('week_id')]
            ))
    
    # Populate the days objects
    for day in day_data:
        if (day[day_columns.index('past_day')]):
            new_user.day_history.append(day_plan(
                total_mileage=day[day_columns.index('day_total_mileage')],
                goal_stimuli=day[day_columns.index('day_goal_stimuli')],
                cycle=day[day_columns.index('day_cycle')],
                expected_rpe=day[day_columns.index('day_expected_rpe')],
                real_rpe=day[day_columns.index('day_real_rpe')],
                complete_score=day[day_columns.index('day_percent_completion')],
                day_id=day[day_columns.index('day_id')]
            ))
        else:
            new_user.day_future.append(day_plan(
                total_mileage=day[day_columns.index('day_total_mileage')],
                goal_stimuli=day[day_columns.index('day_goal_stimuli')],
                cycle=day[day_columns.index('day_cycle')],
                expected_rpe=day[day_columns.index('day_expected_rpe')],
                day_id=day[day_columns.index('day_id')]
            ))
    
    
    return new_user
# Testing
print(populate_user_info(2).age) 

# Column names: 'userid', 'dob', 'sex', 'runningex', 'fivekm', 'goaldate', 'mean_rpe', 'std_rpe', 'user_id', 'total_mileage', 'goal_stimuli', 'cycle', 'expected_rpe', 'real_rpe', 'complete_score', 'month_id', 'month_id', 'total_mileage', 'goal_stimuli', 'cycle', 'expected_rpe', 'real_rpe', 'complete_score', 'week_id', 'week_id', 'total_mileage', 'goal_stimuli', 'cycle', 'expected_rpe', 'real_rpe', 'complete_score'