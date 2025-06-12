import psycopg2
import database_connect
from utils.user_storage.user import user

"""Sends user information to the database."""
def send_user_info(user_info, SQL_user):
    try:
        # Initialize the connection with the database
        database = database_connect
        

        
        # Create a new user object
        user = user()
        
        
        
        
    except Exception as error:
        print(f"Error inserting user info: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
    # END: Database connection and insertion
