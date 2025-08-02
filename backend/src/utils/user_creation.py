import logging
import secrets

# ``email_validator`` is an optional dependency used for validating email
# addresses.  Some environments (e.g., this kata's execution sandbox) do not
# have the library installed.  Import it lazily and provide a very small
# fallback so that the remainder of this module can still be imported and
# exercised in tests without the external package.
try:  # pragma: no cover - exercised indirectly via tests
    from email_validator import validate_email, EmailNotValidError
except Exception:  # pragma: no cover
    import re

    class EmailNotValidError(ValueError):
        """Fallback error raised when an email address is invalid."""

        pass

    def validate_email(addr: str, **kwargs) -> None:
        """Validate an email address using a minimal heuristic.

        The fallback simply ensures there is an ``@`` symbol and a period in
        the domain portion.  It raises ``EmailNotValidError`` if the check
        fails.
        """

        # Basic pattern: ``local@domain.tld`` where each part has at least one
        # character.  This is not RFC compliant but suffices for test usage.
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", addr):
            raise EmailNotValidError("Invalid email address")

# Database utilities are optional during testing.  Import them lazily so that
# the module can be used without a full database stack available.  Tests that
# exercise database functionality can skip appropriately if these imports are
# missing.
try:  # pragma: no cover - simply providing a fallback
    from backend.src.utils.user_storage.user import user  # type: ignore
except Exception:  # pragma: no cover
    user = None  # type: ignore

try:  # pragma: no cover
    from backend.src.utils.SQLutils.user_send import send_user_creds, send_user_all  # type: ignore
    from backend.src.utils.SQLutils.config import DB_CREDENTIALS  # type: ignore
    from backend.src.utils.SQLutils.database_connect import init_db  # type: ignore
except Exception:  # pragma: no cover
    send_user_creds = send_user_all = None  # type: ignore
    DB_CREDENTIALS = {}  # type: ignore
    init_db = None  # type: ignore

logger = logging.getLogger(__name__)

USERNAME_LOC, PASSWORD_LOC = 0, 1
PASS_LEN_REQ = 8


"""Utility validation helpers."""


def validate_address(email: str):
    """Check whether ``email`` is syntactically valid.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: ``True`` if the address is valid, ``False`` otherwise.
    """
    try:
        # ``email_validator`` checks DNS records by default which can make
        # simple unit tests fail when using placeholder domains such as
        # ``example.com``.  Disable deliverability checks so that we only
        # validate the syntactic structure of the address.  The fallback
        # implementation above accepts arbitrary keyword arguments so this
        # call works whether or not the third-party library is installed.
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False

# Add pace estimator so that it only runs once when the user is created.


""" This function creates a new user based on user input.
Full population of the SQL database is performed from the the referenced user object and login information is sent to a seperate table for
long term storage and security. In an the event an SQL query fails, the function will return an error message."""

# def user_create(SQL_username, SQL_password, surveyanswers: list, signup_answers: list):

#     # assign the survey questions to the user object.
#     user_username = signup_answers[0]
#     user_password = signup_answers[1]
#     user_email = signup_answers[2]

#     # Maybe make a is_valid_password function later.
#     if (len(user_password) < PASS_LEN_REQ):
#         raise ValueError("Password must be at least 8 characters long.")

#     # Replace with a secure hashing function
#     hashed_password = hash(user_password)

#     # generate a new user object based on the survey questions.
#     # This will get modified when user is. Don't forget.
#     new_user = user(
#         dob=surveyanswers[0], sex=surveyanswers[1], running_ex=surveyanswers[2],
#         five_km_estimate=surveyanswers[3], goal_date=surveyanswers[4],
#         mean_RPE=surveyanswers[5], STD_RPE=surveyanswers[6])

#     # send all user information into SQL database in appropriate tables.
#     # This includes the user object, the username, password, and email.
#     # The user object is created with a user_id that is generated in the user class.

#     try:
#         # Send the user object to the database.
#         send_user_creds(new_user, SQL_username, SQL_password, signup_answers)

#     except Exception as e:
#         raise RuntimeError(f"Failed to send user credentials: {e}")

#     try:
#         # Send the user object to the database.
#         send_user_all(new_user, SQL_username, SQL_password)

#     except Exception as e:
#         raise RuntimeError(f"Failed to send user data: {e}")

#     return new_user  # Return the user object for further use or confirmation.

#     # Note: The user object is created with a user_id that is generated in the user class.
#     # When a new user is created user.py handles creating a user id.

# """ Testing function for user creation."""
# suveryanswers = [
#     12345, "male", "advanced", "17:45", 4, 5, 2  # Example survey answers
# ]

# signupanswers = [
#     "testuser@gmail.com",  # Email
#     "testuser",  # Username
#     "securepassword",  # Password
# ]


# # user_create(DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"], suveryanswers, signupanswers)


# def login(username: str, password: str, users: dict) -> user:
#     """ A function that takes in a dictionary of the form [username: str, password: str], and checks if the username and password combo exists in the database.
#     If it does, return the user object. If it doesn't, return None.
#     """
#     for user_info, user_obj in users.items():
#         if user_info[USERNAME_LOC] == username and user_info[PASSWORD_LOC] == hash(password):
#             v = 1+1  # Placeholder for any additional logic needed after successful login
#             # Assume this is made:
#             # return SQLutils.get_user(user_obj.user_id)
#     return None


def credential_check(username: str, password: str) -> bool:
    """Verify a username/password pair.

    Args:
        username (str): Account username.
        password (str): Plain text password.

    Returns:
        int | bool: ``user_id`` if credentials are valid, ``0`` otherwise.
    """

    if init_db is None or not DB_CREDENTIALS:
        raise RuntimeError("Database utilities are not configured")

    # initialize the database connection
    conn = init_db(
        username=DB_CREDENTIALS["DB_USERNAME"], pwd=DB_CREDENTIALS["DB_PASSWORD"])

    # open cursor to perform sql queries
    curr = conn.cursor()

    # write query
    query = """ SELECT password, user_id
	                FROM public.user_credentials WHERE username = %s; """
    # fill query with appropriate user ID
    record_to_insert = (username,)

    try:
        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        # fetch the result
        result = curr.fetchone()

        if result is None:
            return 0  # No user found with that username
        # Check if the provided password matches the stored password
        if result[0] == password:
            print("matched")
            return result[1]  # Return user_id if credentials are valid
        else:
            return 0
    except Exception as e:
        logger.exception("Error executing query: %s", e)
        # return 0

    finally:
        # close cursor
        curr.close()
        # close connection
        conn.close()


def user_exists(user_credentials) -> tuple:
    """Check whether a user already exists.

    Args:
        user_credentials (dict): Dictionary with ``email`` and ``username`` keys.

    Returns:
        tuple: ``(True, code)`` if user exists (``code`` 1 for email conflict,
        0 for username). ``(False, user_id)`` otherwise.
    """
    if init_db is None or not DB_CREDENTIALS:
        raise RuntimeError("Database utilities are not configured")

    conn = init_db(DB_CREDENTIALS["DB_USERNAME"],
                   DB_CREDENTIALS["DB_PASSWORD"])
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
            # Generate a new user_id if the user does not exist
            user_id = user.generate_new_id()
            return False, user_id  # User does not exist, return user_id

    except Exception as e:
        logger.exception("Error executing query, %s", e)
        # print("Error during query execution:", e)

    finally:
        curr.close()
        conn.close()


def forgot_password(username: str, new_password: str, email: str) -> bool:
    """Reset a user's password.

    Args:
        username (str): Username to update.
        new_password (str): New password in plain text.
        email (str): Email used for verification.

    Returns:
        bool: ``True`` if the reset succeeded, ``False`` otherwise.
    """

    if init_db is None or not DB_CREDENTIALS:
        raise RuntimeError("Database utilities are not configured")

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
        logger.exception("Error executing query: %s", e)
        # print(f"Error executing query: {e}")
        return False

    finally:
        # close cursor
        curr.close()
        # close connection
        conn.close()
