import psycopg2
import logging
from psycopg2.extras import register_composite
from backend.src.utils.SQLutils.config import DB_CREDENTIALS

# takes in the host name (localhost for database owner).
# Establish connection with the SQL database and return an error message if connection fails.


def init_db(username, pwd):
    try:
        if (username != "postgres"):
            locate = DB_CREDENTIALS["host"]
        else:
            locate = 'localhost'
        # Establish connection
        conn = psycopg2.connect(database="userdatabase",
                                user=username,
                                host=locate,
                                password=pwd,
                                port="5432",
                                connect_timeout=10)

        return conn
    except psycopg2.Error as e:
        logging.exception("Database connection error")
        return None

def db_select(curr, query, user_id):
    """
    Executes a SQL query to select data for a specific user ID.
    
    Parameters:
    - curr: The database cursor.
    - query: The SQL query to execute.
    - user_id: The user ID to filter the query.
    
    Returns:
    - The fetched results from the executed query.
    """
    try:
        # Fill the query with the user ID
        curr.execute(query, (user_id,))
        # Fetch all results from the query
        result = curr.fetchall()
        return result
    except psycopg2.Error as e:
        logging.exception("Error executing query")
        return None


# Takes in prelim survey datapoints and inserts them into the SQL database
def db_insert(curr, user_id, dob, sex, runningex, injury,
              most_recent_injury, longest_run, goal_date, pace_estimate,
              available_days, number_of_days, workout_rpe):
    # write query
    query = """ INSERT INTO public.userlistai(
        user_id, dob, sex, runningex, injury, most_recent_injury, longest_run, 
        goaldate, pace_estimate, available_days, number_of_days, workout_rpe)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
    # fill query with appropriate user ID
    record_to_insert = (user_id, dob, sex, runningex, injury, most_recent_injury,
                        longest_run, goal_date, pace_estimate, available_days,
                        number_of_days, workout_rpe)

    # execute query with filled parameters
    curr.execute(query, record_to_insert)

# Takes in prelim survey datapoints and inserts them into the SQL database


def db_update(curr, user_id, dob, sex, runningex, injury,
              most_recent_injury, longest_run, goal_date, pace_estimate,
              available_days, number_of_days, workout_rpe):
    # write query
    query = """ UPDATE public.userlistai
        SET dob= %s, sex= %s, runningex= %s, injury= %s, most_recent_injury= %s, 
            longest_run= %s, goaldate= %s, pace_estimate= %s, available_days= %s, 
            number_of_days= %s, workout_rpe = %s
            WHERE user_id = %s; """
    # fill query with appropriate user ID
    record_to_insert = (dob, sex, runningex, injury, most_recent_injury,
                        longest_run, goal_date, pace_estimate, available_days,
                        number_of_days, workout_rpe, user_id)

    # execute query with filled parameters
    curr.execute(query, record_to_insert)
