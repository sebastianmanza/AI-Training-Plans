import secrets
from backend.src.utils.user_storage.user import user
from backend.src.utils.SQLutils.user_send import send_user_creds, send_user_all
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.SQLutils.database_connect import init_db

USERNAME_LOC, PASSWORD_LOC = 0, 1
PASS_LEN_REQ = 8


# Add pace estimator so that it only runs once when the user is created.

""" This function creates a new user based on user input.
Full population of the SQL database is performed from the the referenced user object and login information is sent to a seperate table for
long term storage and security. In an the event an SQL query fails, the function will return an error message."""


def user_create(SQL_username, SQL_password, surveyanswers: list, signup_answers: list):

    # assign the survey questions to the user object.
    user_username = signup_answers[0]
    user_password = signup_answers[1]
    user_email = signup_answers[2]

    # Maybe make a is_valid_password function later.
    if (len(user_password) < PASS_LEN_REQ):
        raise ValueError("Password must be at least 8 characters long.")

    # Replace with a secure hashing function
    hashed_password = hash(user_password)

    # generate a new user object based on the survey questions.
    # This will get modified when user is. Don't forget.
    new_user = user(
        dob=surveyanswers[0], sex=surveyanswers[1], running_ex=surveyanswers[2],
        five_km_estimate=surveyanswers[3], goal_date=surveyanswers[4],
        mean_RPE=surveyanswers[5], STD_RPE=surveyanswers[6])

    # send all user information into SQL database in appropriate tables.
    # This includes the user object, the username, password, and email.
    # The user object is created with a user_id that is generated in the user class.

    try:
        # Send the user object to the database.
        send_user_creds(new_user, SQL_username, SQL_password, signup_answers)

    except Exception as e:
        raise RuntimeError(f"Failed to send user credentials: {e}")

    try:
        # Send the user object to the database.
        send_user_all(new_user, SQL_username, SQL_password)

    except Exception as e:
        raise RuntimeError(f"Failed to send user data: {e}")

    return new_user  # Return the user object for further use or confirmation.

    # Note: The user object is created with a user_id that is generated in the user class.
    # When a new user is created user.py handles creating a user id.

""" Testing function for user creation."""
suveryanswers = [
    12345, "male", "advanced", "17:45", 4, 5, 2  # Example survey answers
]

signupanswers = [
    "testuser@gmail.com",  # Email
    "testuser",  # Username
    "securepassword",  # Password
]


# user_create(DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"], suveryanswers, signupanswers)


def login(username: str, password: str, users: dict) -> user:
    """ A function that takes in a dictionary of the form [username: str, password: str], and checks if the username and password combo exists in the database.
    If it does, return the user object. If it doesn't, return None.
    """
    for user_info, user_obj in users.items():
        if user_info[USERNAME_LOC] == username and user_info[PASSWORD_LOC] == hash(password):
            v = 1+1  # Placeholder for any additional logic needed after successful login
            # Assume this is made:
            # return SQLutils.get_user(user_obj.user_id)
    return None


def credential_check(username: str, password: str) -> bool:
    """ A function that checks if the username and password combination exists in the database.
    Returns the user_id if the credentials are valid, 0 if no user is found with that username
    """

    # initialize the database connection
    conn = init_db()

    # open cursor to perform sql queries
    curr = conn.cursor()

    # write query
    query = """ SELECT password, user_id
	                FROM public.user_credentials WHERE username = %s; """
    # fill query with appropriate user ID
    record_to_insert = (username)

    try:
        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        # fetch the result
        result = curr.fetchone()

        if result is None:
            return 0  # No user found with that username

        # Check if the provided password matches the stored password
        if result[0] == hash(password):
            return result[1]  # Return user_id if credentials are valid
    except Exception as e:

        print(f"Error executing query: {e}")
        return 0

    finally:
        # close cursor
        curr.close()
        # close connection
        conn.close()


def user_exists(user_credentials) -> tuple:
    """Checks if the user exists in the database.
    If the user exists, returns True and an error code (1 for email, 0 for username).
    If the user does not exist, returns False and a user_id.
    """
    conn = init_db(DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])
    curr = conn.cursor()

    # write query to check if user exists by email or username
    query = """SELECT email, username FROM public.user_credentials WHERE email = %s OR username = %s;"""
    record_to_insert = (
        user_credentials['email'], user_credentials['username'])

    try:
        curr.execute(query, record_to_insert)
        result = curr.fetchone()

        # Check if the result matches the email and username, return true if they do
        email_match = result[0] == user_credentials['email'] if result else False
        username_match = result[1] == user_credentials['username'] if result else False


        # if the email matches, return True (the user exists, and an error code)
        if email_match:
            return True, 1

        if username_match:
            return True, 0

        if not (email_match or username_match):
            user_id = secrets.randbelow(100000000 - 10000000)
            return False, user_id  # User does not exist, return user_id

    except Exception as e:
        print("Error during query execution:", e)

    finally:
        curr.close()
        conn.close()


def forgot_password(username: str, new_password: str, email: str) -> bool:
    """ A function that resets the password for a user.
    Returns True if successful, False otherwise.
    """

    # checks if the user exists in the database
    if not user_exists(email)[0]:
        print("User does not exist.")
        return False

    # We can now assume the user exists:
    
    # initialize the database connection
    conn = init_db()

    # open cursor to perform sql queries
    curr = conn.cursor()

    # write query
    query = """ UPDATE public.user_credentials SET password = %s WHERE username = %s; """

    record_to_insert = (hash(new_password), username)

    try:
        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        # commit the changes
        conn.commit()

        return True  # Password reset successful
    except Exception as e:
        print(f"Error executing query: {e}")
        return False

    finally:
        # close cursor
        curr.close()
        # close connection
        conn.close()
        
