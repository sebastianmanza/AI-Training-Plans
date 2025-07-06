import sys
import os
# Dynamically find the root directory containing the 'backend' folder
current_dir = os.path.dirname(__file__)
while not os.path.exists(os.path.join(current_dir, "backend")):
    current_dir = os.path.dirname(current_dir)
    if current_dir == "/":  # Stop if we reach the root of the filesystem
        raise RuntimeError(
            "Could not find 'backend' folder in the directory hierarchy.")

# Add the root directory to the Python path
sys.path.append(current_dir)

from collections import namedtuple
from psycopg2.extras import register_composite
from backend.src.utils.user_storage.storage_stacks_and_queues import *
from backend.src.utils.user_storage.day_plan import *
from backend.src.utils.user_storage.week_plan import *
from backend.src.utils.user_storage.month_plan import *
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.SQLutils.database_connect import init_db
from backend.src.utils.user_storage.user import user
from backend.src.utils.SQLutils.database_connect import db_insert, db_update
import psycopg2
from queue import Empty


# Sends user information to the database.
def send_user_info(new_user, username, password):

    try:
        # Initialize the connection with the database
        tryconn = init_db(username, password)
        # open cursor to perform sql queries
        curr = tryconn.cursor()
        # check to see that the user does not already exist
        db_query = """ SELECT * FROM public.userlistai WHERE userid = %s """
        record_to_insert = (new_user.user_id)

        # execute query with filled parameters
        curr.execute(db_query, record_to_insert)

        # now update the information of the existing user within the SQL database
        db_update(username, password, new_user.age, new_user.sex, new_user.five_km_estimate, new_user.goal_date,
                  new_user.running_ex, new_user.mean_RPE, new_user.STD_RPE)

        # make changes in database persistent
        tryconn.commit()
        # close cursor
        curr.close()
        # close connection
        tryconn.close()

    except Exception:

        # inserts as a new row in the database if user does not exist already
        db_insert(username, password, new_user.user_id, new_user.age, new_user.sex, new_user.five_km_estimate, new_user.goal_date, new_user.running_ex,
                  new_user.mean_RPE, new_user.STD_RPE)


# populate past month cycle user infomation within SQL database
def send_month_history(new_user, username, password):

    conn = init_db(username, password)
    # open cursor to perform sql queries
    curr = conn.cursor()

    while new_user.month_history:

        pres = new_user.month_history.pop()

        # write query
        query = """ INSERT INTO public.month_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, month_id, past_month, complete_mileage)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
        # fill query with appropriate user ID

        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (new_user.user_id, pres.total_mileage, pres.goal_stimuli, pres.cycle, pres.expected_rpe, pres.real_rpe,
                            pres.percent_completion, pres.month_id, True, pres.completed_mileage)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        conn.commit()

    # close cursor
    curr.close()
    # close connection
    conn.close()


# populate future month cycle user infomation within SQL database
def send_month_future(new_user, username, password):

    conn = init_db(username, password)
    # open cursor to perform sql queries
    curr = conn.cursor()

    while new_user.month_future:

        if (new_user.month_future.qsize() == 0):
            print("Queue is now empty")
            break

        fut = new_user.month_future.get()

        # write query
        query = """ INSERT INTO public.month_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, month_id, past_month, complete_mileage)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (new_user.user_id, fut.total_mileage, fut.goal_stimuli, fut.cycle, fut.expected_rpe, fut.real_rpe,
                            fut.percent_completion, fut.month_id, False, fut.completed_mileage)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        # make changes in database persistent
        conn.commit()

    # close cursor
    curr.close()
    # close connection
    conn.close()
    print("Connection closed. Script complete.")


# populate past week cycle user infomation within SQL database
def send_week_cycle(new_user, username, password):

    conn = init_db(username, password)
    # open cursor to perform sql queries
    curr = conn.cursor()

    while new_user.week_history:

        pres = new_user.week_history.pop()

        # write query
        query = """ INSERT INTO public.week_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, week_id, past_week, complete_mileage, month_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """
        # fill query with appropriate user ID

        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (new_user.user_id, pres.total_mileage, pres.goal_stimuli, pres.cycle, pres.expected_rpe, pres.real_rpe,
                            pres.percent_completion, pres.week_id, True, pres.completed_mileage, pres.month_id)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        # make changes in database persistent
        conn.commit()

    while new_user.week_future:

        if (new_user.week_future.qsize() == 0):
            print("Queue is now empty")
            break

        fut = new_user.week_future.get()

        # write query
        query = """ INSERT INTO public.week_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, week_id, past_week, complete_mileage, month_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (new_user.user_id, fut.total_mileage, fut.goal_stimuli, fut.cycle, fut.expected_rpe, fut.real_rpe,
                            fut.percent_completion, fut.week_id, False, fut.completed_mileage, fut.month_id)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        # make changes in database persistent
        conn.commit()

    # close cursor
    curr.close()
    # close connection
    conn.close()


# populate day cycle user infomation within SQL database
def send_day_cycle(new_user, username, password):

    conn = init_db(username, password)
    register_composite('trio', conn)  # No errors = good

    workouts = [(1.0, 2.0, 3.0), (1.0, 2.0, 3.0)]

    # open cursor to perform sql queries
    curr = conn.cursor()

    while new_user.day_history:

        pres = new_user.day_history.pop()

        # cast workouts to trio type
        TrioType = register_composite('trio', conn, globally=True).type
        workouts = cast_workouts_to_trios(pres.workouts, TrioType)

        # write query
        query = """ INSERT INTO public.day_cycle(
            user_id, total_mileage, goal_stimuli, lift, expected_rpe, real_rpe, complete_score, past_day, complete_mileage, week_id, workouts)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::trio[]); """
        # fill query with appropriate user ID

        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (new_user.user_id, pres.total_mileage, pres.goal_stimuli, pres.lift, pres.expected_rpe, pres.real_rpe,
                            pres.percent_completion, True, pres.completed_mileage, pres.week_id, workouts)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        # make changes in database persistent
        conn.commit()

    while new_user.day_future:

        if (new_user.day_future.qsize() == 0):
            print("Queue is now empty")
            break

        fut = new_user.day_future.get()

        # cast workouts to trio type
        TrioType = register_composite('trio', conn, globally=True).type
        workouts = cast_workouts_to_trios(fut.workouts, TrioType)

        # write query
        query = """ INSERT INTO public.day_cycle(
            user_id, total_mileage, goal_stimuli, lift, expected_rpe, real_rpe, complete_score, past_day, complete_mileage, week_id, workouts)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::trio[]); """
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (new_user.user_id, fut.total_mileage, fut.goal_stimuli, fut.lift, fut.expected_rpe, fut.real_rpe,
                            fut.percent_completion, False, fut.completed_mileage, fut.week_id, workouts)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        # make changes in database persistent
        conn.commit()

    # close cursor
    curr.close()
    # close connection
    conn.close()


""" To do: update method to check for existing user_id and handle appropriate updating without repeated user inputs"""
# sends username, password, email, and userid into the database


def send_user_creds(new_user, username, password, user_username, user_password, user_email):

    try:

        conn = init_db(username, password)
        # open cursor to perform sql queries
        curr = conn.cursor()

        # prepare query to find or new user credential fields
        query = """ INSERT INTO public.user_credentials(user_id, email, username, password)
                VALUES (%s, %s, %s, %s); """

        record_to_insert = (new_user.user_id, user_username,
                            user_password, user_email)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)

        # make changes in database persistent
        conn.commit()

        # close cursor
        curr.close()
        # close connection
        conn.close()

    except Exception:

        try:

            conn = init_db(username, password)
            # open cursor to perform sql queries
            curr = conn.cursor()

            query = """ UPDATE public.user_credentials email=%s, username=%s, password=%s
                        WHERE user_id=%s; """

            record_to_insert = (
                new_user.user_id, user_username, user_password, user_email)

            # execute query with filled parameters
            curr.execute(query, record_to_insert)

            # make changes in database persistent
            conn.commit()

            # close cursor
            curr.close()
            # close connection
            conn.close()

        except Exception as e:
            print("Error updating user credentials:", e)
            # Handle the error as needed, e.g., log it or raise an exception


def send_user_all(user_id, username, password):

    send_user_info(user_id, username, password)

    send_month_history(user_id, username, password)

    send_month_future(user_id, username, password)

    send_week_cycle(user_id, username, password)

    send_day_cycle(user_id, username, password)


# Trio = namedtuple('Trio', ['x', 'y', 'z'])

def cast_workouts_to_trios(workouts, TrioType):

    return [TrioType(*triplet) for triplet in workouts]


def testing_cycle(username, password):

    conn = init_db(username, password)
    cursor = conn.cursor()
    TrioType = register_composite(
        'trio', conn, globally=True).type  # No errors = good

    raw_workouts = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    # Minimal, valid trio array
    casted_workouts = cast_workouts_to_trios(raw_workouts, TrioType)

    cursor.execute(
        "INSERT INTO day_cycle (user_id, workouts) VALUES (%s, %s::trio[])",
        (999, casted_workouts)
    )
    conn.commit()


# # testing
storage = storage_stacks_and_queues()

new_user = user(19, "male", "advanced", "17:45", 3, 5, 7)


# send_user_info(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])

# #  user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, month_id, past_month, complete_mileage


# #testing month population

# month_one = month_plan.month_plan(100, 1, 2, 10, 3, 99, 99, 10)
# month_two =  month_plan.month_plan(100, 1, 2, 10, 3, 99, 99, 10)
# month_three =  month_plan.month_plan(100, 1, 2, 11, 4, 99, 99, 10)
# month_four =  month_plan.month_plan(100, 1, 2, 11, 4, 99, 99, 10)

# new_user.append_month(month_one)
# new_user.append_month(month_two)

# new_user.append_fut_month(month_two)
# new_user.append_fut_month(month_three)

# send_month_history(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
# send_month_future(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])

# testing week population
'''
week_one = week_plan.week_plan(100, 1, 2, 10, 3, 99, 99, 10)
week_two = week_plan.week_plan(100, 1, 2, 10, 3, 99, 99, 10)
week_three = week_plan.week_plan(100, 1, 2, 11, 4, 99, 99, 10)

new_user.append_week(week_one)
new_user.append_week(week_two)  

new_user.append_fut_week(week_two)
new_user.append_fut_week(week_three)

send_week_cycle(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
'''
# testing day population


# list_of_workouts = [(1, 3, 4), (4, 5, 6)]

# day_one = day_plan(list_of_workouts, 1, False, 10, 3, 99, 99, 10)
# day_two = day_plan(list_of_workouts, 1, False, 10, 3, 99, 99, 10)
# day_three = day_plan(list_of_workouts, 1, False, 11, 4, 99, 99, 10)

# new_user.append_day(day_one)
# new_user.append_day(day_two)

# new_user.append_fut_day(day_two)
# new_user.append_fut_day(day_three)

# send_day_cycle(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])

# testing_cycle(DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])


# print(type(new_user.month_history), len(new_user.month_history))
# print("Queue before sending:", new_user.month_future.qsize())
# print(new_user.month_future.get())
