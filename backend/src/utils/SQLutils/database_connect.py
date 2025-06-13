import psycopg2
from utils.SQLutils.config import DB_CREDENTIALS

    # takes in the host name (localhost for database owner). 
    # Establish connection with the SQL database and return an error message if connection fails.
def init_db(username, pwd):
    try:
        if (username != "postgres"):
            locate = DB_CREDENTIALS["host"]
        else:
            locate = 'localhost'
        # Establish connection
        conn = psycopg2.connect(database = "UserList",
                                user = username,
                                host = locate,
                                password = pwd,
                                port = "5432")
            
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None


        
# Takes in a user ID and retreives their information from the SQL database. 
def db_select(username, pwd, user_id, query):
        
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
        
        # return the result
        return result
    
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        if conn:
            conn.close()
        return None
            

    
        
        

        
        
        
        
        
        
            
            
        
        
        