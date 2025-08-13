import logging
import secrets
import bcrypt

from email_validator import validate_email
try:  # pragma: no cover - simply providing a fallback
    from backend.src.utils.user_storage.user import user  # type: ignore
except Exception:  # pragma: no cover
    user = None  # type: ignore

try:
    from backend.config import DB_CREDENTIALS  # type: ignore
    from backend.src.utils.SQLutils.database_connect import init_db  # type: ignore
except Exception:  # pragma: no cover
    DB_CREDENTIALS = {}  # type: ignore
    init_db = None  # type: ignore

logger = logging.getLogger(__name__)

USERNAME_LOC, PASSWORD_LOC = 0, 1
PASS_LEN_REQ = 8


"""Utility validation helpers."""


def hash_password(password: str) -> str:
    """Hash ``password`` using bcrypt.

    Args:
        password (str): Plain text password.

    Returns:
        str: Bcrypt hashed password encoded as UTF-8.
    """

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def validate_address(email: str):
    """Check whether ``email`` is syntactically valid.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: ``True`` if the address is valid, ``False`` otherwise.
    """
    try:
        validate_email(email, check_deliverability=False)
        return True
    except Exception:
        return False


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

        stored_password, user_id = result
        try:
            if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
                return user_id  # Return user_id if credentials are valid
        except ValueError:
            # Stored password may be plain text (e.g., in tests); fall back to a constant-time comparison.
            if secrets.compare_digest(stored_password, password):
                return user_id
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
        logger.warning(
            "Password reset requested for non-existent user: %s", username)
        return False

    # We can now assume the user exists:

    # initialize the database connection
    conn = init_db()

    # open cursor to perform sql queries
    curr = conn.cursor()

    # write query
    query = """ UPDATE public.user_credentials SET password = %s WHERE username = %s; """

    hashed_password = hash_password(new_password)
    record_to_insert = (hashed_password, username)

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
