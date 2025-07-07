import psycopg2
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
        conn = psycopg2.connect(database="UserList",
                                user=username,
                                host=locate,
                                password=pwd,
                                port="5432",
                                connect_timeout=10)

        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None


# Takes in a user ID and retreives their information from the SQL database.
def db_select(username, pwd, user_id, query, return_cursor=False):

    conn = init_db(username, pwd)

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
        print(f"Error executing query: {e}")
        if conn:
            conn.close()
        return None


# Takes in prelim survey datapoints and inserts them into the SQL database
def db_insert(username, pwd, user_id, dob, sex, runningex, fivekm, goaldate, mean_rpe, std_rpe):

    conn = init_db(username, pwd)
    # open cursor to perform sql queries
    curr = conn.cursor()

    # write query
    query = """ INSERT INTO public.userlistai(
        user_id, dob, sex, runningex, fivekm, goaldate, mean_rpe, std_rpe)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s); """
    # fill query with appropriate user ID
    record_to_insert = (user_id, dob, sex, runningex,
                        fivekm, goaldate, mean_rpe, std_rpe)

    # execute query with filled parameters
    curr.execute(query, record_to_insert)
    # make changes in database persistent
    conn.commit()
    # close cursor
    curr.close()

# Takes in prelim survey datapoints and inserts them into the SQL database


def db_update(username, pwd, userid, dob, sex, runningex, fivekm, goaldate, mean_rpe, std_rpe):

    conn = init_db(username, pwd)
    # open cursor to perform sql queries
    curr = conn.cursor()

    # write query
    query = """ UPDATE public.userlistai
        SET dob=%s, sex=%s, runningex=%s, fivekm=%s, goaldate=%s, mean_rpe=%s, std_rpe=%s
        WHERE userid = %s; """
    # fill query with appropriate user ID
    record_to_insert = (userid, dob, sex, runningex,
                        fivekm, goaldate, mean_rpe, std_rpe)

    # execute query with filled parameters
    curr.execute(query, record_to_insert)
    # make changes in database persistent
    conn.commit()
    # close cursor
    curr.close()
    # close connection
