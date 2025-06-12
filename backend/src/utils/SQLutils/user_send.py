import psycopg2
from database_connect import init_db
from backend.src.utils.user_storage.user import user

"""Sends user information to the database."""
def send_user_info(user_info, SQL_host, SQL_password):
    try:
        # Initialize the connection with the database
        init_db(SQL_host, SQL_password)
        
        # Create a new user object
        user = user()
        
        
        
        
    except Exception as error:
        print(f"Error inserting user info: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
    # END: Database connection and insertion
