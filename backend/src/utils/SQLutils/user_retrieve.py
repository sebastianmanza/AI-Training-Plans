import json
from backend.src.utils.user_storage.day_plan import day_plan
from backend.src.utils.user_storage.week_plan import week_plan
from backend.src.utils.user_storage.month_plan import month_plan
from backend.config import DB_CREDENTIALS
from backend.src.utils.user_storage.user import user
from backend.src.utils.SQLutils.database_connect import db_select, init_db
import psycopg2
from psycopg2.extras import register_composite, NamedTupleCursor
import logging

logger = logging.getLogger(__name__)

class UserNotFoundError(Exception):
    """Exception raised when a user is not found in the database."""

    def __init__(self, user_id):
        """Record the missing ``user_id``.

        Args:
            user_id (int): Identifier that was not found.
        """
        super().__init__(f"No user found with ID {user_id}.")

class DatabaseConnectionError(Exception):
    """Exception raised for errors in the database connection."""
    pass

class QueryExecutionError(Exception):
    """Exception raised for errors during query execution."""
    pass

def convert_trio_types_to_tuples(list_of_trios: list):
    """Cast composite trio objects to plain tuples.

    Args:
        list_of_trios (list): Sequence of ``Trio`` composite objects.

    Returns:
        list: List of ``tuple`` objects representing the trios.
    """
    return [tuple(trio) for trio in list_of_trios]


def convert_trio_type_to_tuples(trio: tuple):
    """Cast a ``Trio`` composite to a tuple.

    Args:
        trio (tuple): Composite trio object.

    Returns:
        tuple: ``(stim, rpe, dist)`` representation or zeros if ``trio`` is ``None``.
    """
    return tuple(trio) if trio else (0.0, 0.0, 0.0)


def retrieve_user_info(user_id: int, username: str, pwd: str):
    """Fetch a user's information and related training plans.

    Args:
        user_id (int): Identifier of the user to retrieve.
        username (str): Database username.
        pwd (str): Database password.

    Returns:
        dict: Dictionary with keys ``user_info``, ``months``, ``weeks`` and ``days``
        mapping to lists of records.

    Raises:
        UserNotFoundError: If the user does not exist.
        DatabaseConnectionError: If there is a connection or execution error.
    """
    # Prepare the queries
    user_query = """
            SELECT 
                user_id, 
                dob, 
                sex, 
                runningex, 
                injury, 
                goaldate, 
                most_recent_injury, 
                longest_run, 
                pace_estimate, 
                workout_rpe, 
                available_days, 
                number_of_days
            FROM userlistai
            WHERE user_id = %s;
            """

    month_query = """
            SELECT 
                total_mileage AS month_total_mileage, 
                goal_stimuli AS month_goal_stimuli, 
                cycle AS month_cycle, 
                expected_rpe AS month_expected_rpe,
                complete_mileage AS month_completed_mileage, 
                complete_score AS month_percent_completion,
                real_rpe AS month_real_rpe, 
                month_id, 
                past_month
            FROM month_cycle
            WHERE user_id = %s;
        """

    week_query = """
            SELECT 
                total_mileage AS week_total_mileage, 
                goal_stimuli AS week_goal_stimuli, 
                cycle AS week_cycle, 
                expected_rpe AS week_expected_rpe,
                complete_mileage AS week_completed_mileage, 
                complete_score AS week_percent_completion,
                real_rpe AS week_real_rpe, 
                week_id, 
                past_week, 
                month_id
            FROM week_cycle
            WHERE user_id = %s;
        """

    day_query = """
            SELECT 
                total_mileage AS day_total_mileage, 
                workouts AS day_workouts, 
                goal_stimuli AS day_goal_stimuli, 
                lift AS day_cycle, 
                expected_rpe AS day_expected_rpe,
                complete_mileage AS day_completed_mileage, 
                complete_score AS day_percent_completion,
                real_rpe AS day_real_rpe, 
                past_day, 
                week_id, 
                day_id
            FROM day_cycle
            WHERE user_id = %s;
        """
    conn = init_db(username, pwd)
    try:
        register_composite("trio", conn, globally=True)

        with conn.cursor(cursor_factory=NamedTupleCursor) as curr:
            user_info = db_select(curr, user_query, user_id)

            if not user_info:
                raise UserNotFoundError(user_id)

            curr.execute(month_query, (user_id,))
            month_info = curr.fetchall()

            curr.execute(week_query, (user_id,))
            week_info = curr.fetchall()

            curr.execute(day_query, (user_id,))
            day_info = curr.fetchall()

            return {
                "user_info": user_info,
                "months": month_info,
                "weeks": week_info,
                "days": day_info
            }

    except psycopg2.Error as e:
        logger.error(f"Database error: {e}")
        raise DatabaseConnectionError("Failed to connect to the database.")
    finally:
        conn.close()


def populate_user_info(user_id):
    """Return a fully populated :class:`user` instance.

    Args:
        user_id (int): Identifier of the user to build.

    Returns:
        user: ``user`` object with history and future training plans loaded.

    Raises:
        UserNotFoundError: If no user with ``user_id`` exists.
    """
    # Retrieve user information
    user_data = retrieve_user_info(
        user_id, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])

    if not user_data:
        logger.exception(f"No user found with ID {user_id}.")
        raise UserNotFoundError(user_id)

    # Create a new user object
    u = user_data['user_info'][0]
    new_user = user(
        dob = u.dob,
        sex = u.sex,
        running_ex = u.runningex,
        injury = u.injury,
        most_recent_injury = u.most_recent_injury,
        longest_run = u.longest_run,
        goal_date = u.goaldate,
        pace_estimates = u.pace_estimate,
        available_days = u.available_days,
        number_of_days = u.number_of_days,
        user_id = u.user_id,
        workout_RPE = u.workout_rpe,
    )

    # Populate the months objects
    for month in user_data['months']:
        new_month = month_plan(
            total_mileage=month.month_total_mileage,
            goal_stimuli=convert_trio_type_to_tuples(month.month_goal_stimuli),
            cycle=month.month_cycle,
            expected_rpe=month.month_expected_rpe,
            real_rpe=month.month_real_rpe,
            percent_completion=month.month_percent_completion,
            month_id=month.month_id,
            completed_mileage=month.month_completed_mileage
        )
        if month.past_month:
            new_user.month_history.append(new_month)
        else:
            new_user.month_future.put(new_month)

    # Populate the weeks objects
    for week in user_data['weeks']:
        new_week = week_plan(
            total_mileage=week.week_total_mileage,
            goal_stimuli=convert_trio_type_to_tuples(week.week_goal_stimuli),
            cycle=week.week_cycle,
            expected_rpe=week.week_expected_rpe,
            real_rpe=week.week_real_rpe,
            percent_completion=week.week_percent_completion,
            week_id=week.week_id,
            month_id=week.month_id,
            completed_mileage=week.week_completed_mileage
        )
        
        if week.past_week:
            new_user.week_history.append(new_week)
        else:
            new_user.week_future.put(new_week)

    # Populate the days objects
    for day in user_data['days']:
        new_day = day_plan(
            total_mileage=day.day_total_mileage,
            workouts=convert_trio_types_to_tuples(day.day_workouts),
            goal_stimuli=convert_trio_type_to_tuples(day.day_goal_stimuli),
            lift=day.day_cycle,
            expected_rpe=day.day_expected_rpe,
            real_rpe=day.day_real_rpe,
            percent_completion=day.day_percent_completion,
            day_id=day.day_id,
            week_id=day.week_id
        )
        if day.past_day:
            new_user.day_history.append(new_day)
        else:
            new_user.day_future.put(new_day)
            
    all_months = list(new_user.month_history) + list(new_user.month_future.queue)
    month_by_id = {m.month_id: m for m in all_months}
    all_weeks = list(new_user.week_history) + list(new_user.week_future.queue)
    for w in all_weeks:
        month_by_id[w.month_id].weeks.append(w)

    week_by_id = {w.week_id: w for w in all_weeks}
    all_days = list(new_user.day_history) + list(new_user.day_future.queue)
    for d in all_days:
        week_by_id[d.week_id].days.append(d)
    return new_user
