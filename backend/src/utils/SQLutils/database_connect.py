"""Helpers for connecting to and querying the PostgreSQL database."""

import psycopg2
import logging
from backend.config import DB_CREDENTIALS
import backend.config as cfg

logger = logging.getLogger(__name__)

# takes in the host name (localhost for database owner).
# Establish connection with the SQL database and return an error message if connection fails.


def init_db(username, pwd):
    """Create a connection to the PostgreSQL database.

    Args:
        username (str): Database username.
        pwd (str): Password for the given username.

    Returns:
        connection | None: A connection instance on success, otherwise ``None``.

    Raises:
        psycopg2.Error: If the connection attempt fails.
    """
    try:
        if (username != "postgres"):
            locate = cfg.DB_CREDENTIALS["host"]
        else:
            locate = "localhost"
        # Establish connection
        logger.debug("Connecting to database at %s as user %s", locate, username)
        conn = psycopg2.connect(database="userdatabase",
                                user=username,
                                host=locate,
                                password=pwd,
                                port="5432",
                                connect_timeout=10)

        return conn
    except psycopg2.Error as e:
        logger.exception("Database connection error,", exc_info=e) # Log the error
        return None

def db_select(curr, query, user_id):
    """Execute ``query`` using ``user_id`` as a parameter.

    Args:
        curr (cursor): Active database cursor.
        query (str): Parameterized SQL query.
        user_id (int): Target user identifier.

    Returns:
        list | None: Query results or ``None`` if execution fails.

    Raises:
        psycopg2.Error: If execution of the query fails.
    """
    try:
        # Fill the query with the user ID
        curr.execute(query, (user_id,))
        # Fetch all results from the query
        result = curr.fetchall()
        return result
    except psycopg2.Error as e:
        logger.exception("Error executing query")
        return None


def db_insert(curr, user_id, dob, sex, runningex, injury,
              most_recent_injury, longest_run, goal_date, pace_estimate,
              available_days, number_of_days, workout_rpe):
    """Insert a user into ``userlistai``.

    Args:
        curr (cursor): Active database cursor.
        user_id (int): User identifier.
        dob (str): Date of birth.
        sex (str): Sex of the user.
        runningex (str): Running experience level.
        injury (int): Number of significant injuries.
        most_recent_injury (int): Months since most recent injury.
        longest_run (int): Longest run distance.
        goal_date (str): Primary goal race date.
        pace_estimate (list): Serialized list of pace estimates.
        available_days (list): Days available for training.
        number_of_days (int): Desired running days per week.
        workout_rpe (str): JSON string of workout RPE values.

    Returns:
        bool: ``True`` on success, ``False`` on failure.
    """
    # write query
    query = """ INSERT INTO public.userlistai(
        user_id, dob, sex, runningex, injury, most_recent_injury, longest_run, 
        goaldate, pace_estimate, available_days, number_of_days, workout_rpe)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
    # fill query with appropriate user ID
    record_to_insert = (user_id, dob, sex, runningex, injury, most_recent_injury,
                        longest_run, goal_date, pace_estimate, available_days,
                        number_of_days, workout_rpe)

    try:
        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        return True
    except psycopg2.Error:
        logger.exception("Failed to insert user_id=%s", user_id)
        curr.connection.rollback()
        return False

# Takes in prelim survey datapoints and inserts them into the SQL database


def db_update(curr, user_id, dob, sex, runningex, injury,
              most_recent_injury, longest_run, goal_date, pace_estimate,
              available_days, number_of_days, workout_rpe):
    """Update an existing row in ``userlistai``.

    Args:
        curr (cursor): Active database cursor.
        user_id (int): Identifier of the user record to update.
        dob, sex, runningex, injury, most_recent_injury, longest_run,
        goal_date, pace_estimate, available_days, number_of_days,
        workout_rpe: See :func:`db_insert` for parameter descriptions.

    Returns:
        bool: ``True`` on success, ``False`` on failure.
    """
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

    try:
        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        return True
    except psycopg2.Error:
        logger.exception("Failed to update user_id=%s", user_id)
        curr.connection.rollback()
        return False
