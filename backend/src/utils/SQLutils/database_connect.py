import psycopg2

class database_connect:
    
    # takes in the host name (localhost for database owner). 
    # Establish connection with the SQL database and return an error message if connection fails.
    def init_db(username, pwd):
        try:
            if (username != "postgres"):
                locate = 'remote_host'
            else:
                locate = 'localhost'
            # Establish connection
            conn = psycopg2.connect(database = "UserListAi",
                                    user = username,
                                    host = locate,
                                    password = pwd,
                                    port = "5432")
            return conn
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            return None
        
    # Takes in a user ID and retreives their information from the SQL database. 
    def db_select(username, pwd, user_id):
        
        conn = database_connect.init_db(username, pwd)
        # open cursor to perform sql queries
        curr = conn.cursor()
        
        # perpare the query 
        database_query = (""" SELECT %s, dob, sex, runningex, fivekm, goaldate
                                FROM public.userlistai; """)
        # fill query with appropriate user ID
        record_to_insert = (user_id)
        
        # execute query with filled parameters
        curr.execute(database_query, record_to_insert)
        # make changes in database persistent
        conn.commit()
        # close cursor
        curr.close()
            
    
    # takes in a user ID and updates given parameters
    # def db_update(user_id, dob, sex, ):

    
        
        

        
        
        
        
        
        
            
            
        
        
        