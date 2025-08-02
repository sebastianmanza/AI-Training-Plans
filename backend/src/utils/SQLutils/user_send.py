import logging
from psycopg2.extras import register_composite, execute_batch
from backend.src.utils.user_storage.storage_stacks_and_queues import *
from backend.src.utils.user_storage.day_plan import *
from backend.src.utils.user_storage.week_plan import *
from backend.src.utils.user_storage.month_plan import *
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.SQLutils.database_connect import init_db
from backend.src.utils.SQLutils.database_connect import db_insert, db_update
from queue import Empty
import json

logger = logging.getLogger(__name__)


def send_user_info(new_user, curr):
    """Insert or update the primary user record.

    Args:
        new_user (user): User object containing information to store.
        curr (cursor): Active database cursor.

    Returns:
        bool: ``True`` if the record was written successfully, ``False`` otherwise.
    """

    # Check if user already exists
    check_query = """SELECT 1 FROM public.userlistai WHERE user_id = %s;"""
    curr.execute(check_query, (new_user.user_id,))
    exists = curr.fetchone()

    # convert workout_RPE dictionary to JSON to allow SQL to handle data properly
    workout_RPE_JSON = json.dumps(new_user.workout_RPE)

    if exists:
        # Update existing user
        return db_update(
            curr,
            new_user.user_id, new_user.dob, new_user.sex, new_user.running_ex, new_user.injury,
            new_user.most_recent_injury, new_user.longest_run, new_user.goal_date,
            new_user.pace_estimates, new_user.available_days, new_user.number_of_days, workout_RPE_JSON
        )
    # Insert new user
    return db_insert(
        curr,
        new_user.user_id, new_user.dob, new_user.sex, new_user.running_ex, new_user.injury,
        new_user.most_recent_injury, new_user.longest_run, new_user.goal_date,
        new_user.pace_estimates, new_user.available_days, new_user.number_of_days, workout_RPE_JSON
    )

def send_month_cycle(new_user, curr):
    """Insert month plans for ``new_user``.

    Args:
        new_user (user): User instance whose ``month_history`` and ``month_future`` contain
            month plans to send.
        curr (cursor): Active database cursor.

    Returns:
        None
    """
    
    query = """ INSERT INTO public.month_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe,
            complete_score, month_id, past_month, complete_mileage)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
    to_send = []

    # Load the month history and future from the user's data structure
    while new_user.month_history:
        month = new_user.month_history.pop()
        to_send.append((
            new_user.user_id, month.total_mileage, month.goal_stimuli,
            month.cycle, month.expected_rpe, month.real_rpe,
            month.percent_completion, month.month_id,
            True, month.completed_mileage
        ))
        
    while not new_user.month_future.empty():
        month = new_user.month_future.get()
        
        to_send.append((
            new_user.user_id, month.total_mileage, month.goal_stimuli,
            month.cycle, month.expected_rpe, month.real_rpe,
            month.percent_completion, month.month_id,
            False, month.completed_mileage
        ))

    if to_send:
        execute_batch(curr, query, to_send, page_size=100)
        

def send_week_cycle(new_user, curr):
    """Insert week plans for ``new_user``.

    Args:
        new_user (user): User instance containing week plan history and future queues.
        curr (cursor): Active database cursor.

    Returns:
        None
    """

    query = """ INSERT INTO public.week_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, 
            complete_score, week_id, past_week, complete_mileage, month_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """
    
    to_send = []
    
    # Load the week history and future from the user's data structure        
    while new_user.week_history:
        week = new_user.week_history.pop()
        to_send.append((
            new_user.user_id, week.total_mileage, week.goal_stimuli,
            week.cycle, week.expected_rpe, week.real_rpe,
            week.percent_completion, week.week_id,
            True, week.completed_mileage, week.month_id
        ))
        
    while not new_user.week_future.empty():
        week = new_user.week_future.get()
        to_send.append((
            new_user.user_id, week.total_mileage, week.goal_stimuli,
            week.cycle, week.expected_rpe, week.real_rpe,
            week.percent_completion, week.week_id,
            False, week.completed_mileage, week.month_id
        ))

    if to_send:
        execute_batch(curr, query, to_send, page_size=100)    


# populate day cycle user infomation within SQL database
def send_day_cycle(new_user, curr, TrioType):
    """Persist day plans for ``new_user``.

    Args:
        new_user (user): User instance containing ``day_history`` and ``day_future`` stacks.
        curr (cursor): Active database cursor.
        TrioType (type): Registered composite representing a trio.

    Returns:
        None
    """

    query = """ INSERT INTO public.day_cycle(
        user_id, day_id, total_mileage, goal_stimuli, lift, expected_rpe, real_rpe, 
        complete_score, past_day, complete_mileage, week_id, workouts)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::trio[]); """
        
        
    to_send = []
    
    # Load the day history and future from the user's data structure
    # Note: The day_history and day_future are expected to be stacks/queues
    # that contain day_plan objects with the necessary attributes.
    while new_user.day_history:
        day = new_user.day_history.pop()
        workouts = cast_workouts_to_trios(day.workouts, TrioType)
        to_send.append((
            new_user.user_id, day.day_id, day.total_mileage, day.goal_stimuli,
            day.lift, day.expected_rpe, day.real_rpe,
            day.percent_completion, True,
            day.completed_mileage, day.week_id, workouts
        ))

    while not new_user.day_future.empty():
        day = new_user.day_future.get()

        workouts = cast_workouts_to_trios(day.workouts, TrioType)

        to_send.append((
            new_user.user_id, day.day_id, day.total_mileage, day.goal_stimuli,
            day.lift, day.expected_rpe, day.real_rpe,
            day.percent_completion, False, day.completed_mileage,
            day.week_id, workouts
        ))

    if to_send:
        execute_batch(curr, query, to_send, page_size=100)


def send_user_creds(user_id, username, password, login_info):
    """Insert or update the user's login credentials.

    Args:
        user_id (int): Identifier for the user.
        username (str): Database username used for the connection.
        password (str): Password for ``username``.
        login_info (dict): Mapping containing ``email``, ``username`` and ``password`` keys.

    Returns:
        None

    Raises:
        Exception: If any database operation fails.
    """

    conn = init_db(username, password)
    curr = conn.cursor()

    try:
        check_query = """
            SELECT 1 FROM public.user_credentials WHERE user_id = %s;
        """
        curr.execute(check_query, (user_id,))
        exists = curr.fetchone()

        if exists:
            update_query = """
                UPDATE public.user_credentials
                SET email = %s, username = %s, password = %s
                WHERE user_id = %s;
            """

            record = (login_info['email'], login_info['username'],
                      login_info['password'], user_id)
            curr.execute(update_query, record)
        else:
            insert_query = """
                INSERT INTO public.user_credentials(user_id, email, username, password)
                VALUES (%s, %s, %s, %s);
            """
            record = (
                user_id, login_info['email'], login_info['username'], login_info['password'])
            curr.execute(insert_query, record)

        conn.commit()

    except Exception:
        conn.rollback()
        logger.exception(
            "Failed to insert credentials for user_id=%s", user_id)

    finally:
        curr.close()
        conn.close()


def send_user_all(user, username, password):
    """Persist all structures associated with ``user``.

    Args:
        user (user): User instance whose data is being stored.
        username (str): Database username.
        password (str): Database password.

    Returns:
        bool: ``True`` on success, ``False`` if any step fails.
    """
    try:
        conn = init_db(username, password)
        curr = conn.cursor()

        caster = register_composite('trio', conn, globally=True)
        TrioType = caster.type

        if not send_user_info(user, curr):
            conn.rollback()
            logger.error("Failed to persist user record for user_id=%s", user.user_id)
            return False

        # send_user_creds(user_id, username, password, login_info)

        send_month_cycle(user, curr)

        send_week_cycle(user, curr)

        send_day_cycle(user, curr, TrioType)

        conn.commit()
        return True
    except Exception:
        conn.rollback()
        logger.exception("Failed to send all user data for user_id=%s", user.user_id)
        return False
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()


def cast_workouts_to_trios(workouts, TrioType):
    """Convert raw workout tuples to ``Trio`` composites.

    Args:
        workouts (list): List of ``(stim, rpe, dist)`` tuples.
        TrioType (type): Registered composite representing a trio.

    Returns:
        list: List of ``TrioType`` objects.
    """
    return [TrioType(*triplet) for triplet in workouts]

