import psycopg2
from backend.src.utils.SQLutils.database_connect import db_select
from backend.src.utils.user_storage.user import user

def retrieve_user_info(user_id: int, username, pwd) -> user:
    """
    Retrieves user information from the database and populates it in a user object.
    
    Args:
        user_id (int): The ID of the user to retrieve.
        username (str): The username for database connection.
        pwd (str): The password for database connection.
    
    Returns:
        user: An instance of the user class containing user details.
    """
    # Prepare the query
    query = """ SELECT u.*, m.*, w.*, d.*
                FROM userlistai u
                LEFT JOIN month_cycle m ON u.userid = m.user_id
                LEFT JOIN week_cycle w ON m.month_id = w.month_id
                LEFT JOIN day_cycle d ON w.week_id = d.week_id
                WHERE u.userid = %s;
            """
    
    # Run the query using db_select, returns list of tuples, with each one representing a row.
    user_info = db_select(username, pwd, user_id, query)
    
    
    return user_info


# Testing
print(retrieve_user_info(1, 'sebastian', '85581')) 