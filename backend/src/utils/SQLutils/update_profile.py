from backend.src.utils.SQLutils.database_connect import init_db
from backend.src.utils.SQLutils.config import DB_CREDENTIALS
from backend.src.utils.user_creation import validate_address

def update_user_email(db_username, db_password, user_id, updated_email: str):
    """ this function takes in the updated email inputted by the user and updates it in the SQL database"""

    valid = validate_address(updated_email)

    # check to see that that updated email is in the correct format
    if (valid):

        conn = init_db(db_username, db_password)
        curr = conn.cursor()

        query = """ SELECT email FROM public.user_credentials
                    WHERE user_id=%s; """

        record_to_insert = (user_id,)

        # queried email string
        email_returned = curr.execute(query, record_to_insert)

        if (email_returned == updated_email):
            raise ValueError("input is the same as previous email")

        conn.commit()

        query = """ UPDATE public.user_credentials
                    email=?
                    WHERE <condition>; """

        record_to_insert = (updated_email,)

        curr.execute(query, record_to_insert)

        curr.close()
        curr.close()

    # else:

    # def update_user_username(db_username, db_password, user_id, updated_username: str)
