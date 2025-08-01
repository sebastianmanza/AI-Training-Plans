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

def send_user_info(new_user, curr):
    """Sends user information to the database. If the user already exists, updates their information; otherwise, inserts a new record.
    Args: 
        new_user (User): An instance of the User class containing user information.
        curr (cursor): The database cursor to execute SQL commands."""
        
    # Check if user already exists
    check_query = """SELECT 1 FROM public.userlistai WHERE user_id = %s;"""
    curr.execute(check_query, (new_user.user_id,))
    exists = curr.fetchone()

    # convert workout_RPE dictionary to JSON to allow SQL to handle data properly
    workout_RPE_JSON = json.dumps(new_user.workout_RPE)

    if exists:
        # Update existing user
        db_update(
            curr,
            new_user.user_id, new_user.dob, new_user.sex, new_user.running_ex, new_user.injury,
            new_user.most_recent_injury, new_user.longest_run, new_user.goal_date,
            new_user.pace_estimates, new_user.available_days, new_user.number_of_days, workout_RPE_JSON
        )
    else:
        # Insert new user
        db_insert(
            curr,
            new_user.user_id, new_user.dob, new_user.sex, new_user.running_ex, new_user.injury,
            new_user.most_recent_injury, new_user.longest_run, new_user.goal_date,
            new_user.pace_estimates, new_user.available_days, new_user.number_of_days, workout_RPE_JSON
        )

def send_month_cycle(new_user, curr):
    """Send month cycle data to the database.
    Args:
        new_user (User): An instance of the User class containing user information.
        curr (cursor): The database cursor to execute SQL commands.
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
        
    while True:
        try:
            month = new_user.month_future.get_nowait()
        except Empty:
            # If the queue is empty, break the loop
            break
        
        to_send.append((
            new_user.user_id, month.total_mileage, month.goal_stimuli,
            month.cycle, month.expected_rpe, month.real_rpe,
            month.percent_completion, month.month_id,
            False, month.completed_mileage
        ))

    if to_send:
        execute_batch(curr, query, to_send, page_size=100)
        

def send_week_cycle(new_user, curr):
    """Send week cycle data to the database.
    Args:
        new_user (User): An instance of the User class containing user information.
        curr (cursor): The database cursor to execute SQL commands.
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
        
    while True:
        try:
            week = new_user.week_future.get_nowait()
        except Empty:
            # If the queue is empty, break the loop
            break
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
        to_send.append(
            new_user.user_id, day.day_id, day.total_mileage, day.goal_stimuli,
            day.lift, day.expected_rpe, day.real_rpe,
            day.percent_completion, True,
            day.completed_mileage, day.week_id, workouts
        )

    while True:
        try:
            fut = new_user.day_future.get_nowait()
        except Empty:
            # If the queue is empty, break the loop
            break

        workouts = cast_workouts_to_trios(fut.workouts, TrioType)

        to_send.append((
            new_user.user_id, fut.day_id, fut.total_mileage, fut.goal_stimuli,
            fut.lift, fut.expected_rpe, fut.real_rpe,
            fut.percent_completion, False, fut.completed_mileage,
            fut.week_id, workouts
        ))

    if to_send:
        execute_batch(curr, query, to_send, page_size=100)


def send_user_creds(user_id, username, password, login_info):
    """
    Sends user credentials to the database. If the user already exists, 
    updates their credentials; otherwise, inserts a new record.

    Args:
        user_id (int): The unique identifier for the user.
        username (str): The username of the user.
        password (str): The password of the user.
        login_info (dict): A dictionary containing 'email', 'username', and 'password' keys.

    Raises:
        Exception: If there is an error during the database operation.
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

    except Exception as e:
        conn.rollback()
        logging.exception(
            "Failed to insert credentials for user_id=%s", user_id)

    finally:
        curr.close()
        conn.close()


def send_user_all(user, username, password):

    try:
        conn = init_db(username, password)
        curr = conn.cursor()

        caster = register_composite('trio', conn, globally=True)
        TrioType = caster.type
        send_user_info(user, curr)

        # send_user_creds(user_id, username, password, login_info)

        send_month_cycle(user, curr)

        send_week_cycle(user, curr)

        send_day_cycle(user, curr, TrioType)

        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error("Failed to send all user data for user_id=%s", user)
    finally:
        if curr:
            curr.close()
        if conn:
            conn.close()


def cast_workouts_to_trios(workouts, TrioType):

    return [TrioType(*triplet) for triplet in workouts]