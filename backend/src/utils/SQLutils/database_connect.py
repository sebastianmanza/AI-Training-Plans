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
        # print(f"Database connection error: {e}")
        return None


init_db(DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])


# Takes in a user ID and retreives their information from the SQL database.
def db_select(username, pwd, user_id, query, return_cursor=False):

    conn = init_db(username, pwd)
    register_composite("trio", conn, globally=True)

    # Check that the connection worked
    if conn is None:
        print("Failed to connect to the database.")
        return None

    try:
        # open cursor to perform sql queries
        curr = conn.cursor()

        # fill query with appropriate user ID
        user_to_retrieve = (user_id)

        # execute query with filled parameters
        curr.execute(query, (user_to_retrieve,))

        # fetch all results from the query
        result = curr.fetchall()

        # close cursor
        curr.close()

        # close connection
        conn.close()

        if return_cursor:
            # Return the cursor along with the result
            return result, curr

        # return the result
        return result

    except psycopg2.Error as e:
        logging.exception("Error executing query")
        if conn:
            conn.close()
        return None


# Takes in prelim survey datapoints and inserts them into the SQL database
def db_insert(username, pwd, user_id, dob, sex, runningex, injury,
              most_recent_injury, longest_run, goal_date, pace_estimate,
              available_days, number_of_days, workout_rpe):

    conn = init_db(username, pwd)
    # open cursor to perform sql queries
    curr = conn.cursor()

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
    # make changes in database persistent
    conn.commit()
    # close cursor
    curr.close()

# Takes in prelim survey datapoints and inserts them into the SQL database


def db_update(username, pwd, user_id, dob, sex, runningex, injury,
              most_recent_injury, longest_run, goal_date, pace_estimate,
              available_days, number_of_days, workout_rpe):

    conn = init_db(username, pwd)
    # open cursor to perform sql queries
    curr = conn.cursor()

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
    # make changes in database persistent
    conn.commit()
    # close cursor
    curr.close()
    # close connection
