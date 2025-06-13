import psycopg2
    
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
def db_select(username, pwd, user_id, query):
        
    conn = init_db(username, pwd)
    # open cursor to perform sql queries
    curr = conn.cursor()
        
    # fill query with appropriate user ID
    record_to_insert = (user_id)
        
    # execute query with filled parameters
    curr.execute(query, record_to_insert)
    # make changes in database persistent
    conn.commit()
    # close cursor
    curr.close()
            

# Takes in prelim survey datapoints and inserts them into the SQL database
def db_insert(username, pwd, user_id, dob, sex, runningex, fivekm, goaldate, mean_rpe, std_rpe):
        
    conn = init_db(username, pwd)
    # open cursor to perform sql queries
    curr = conn.cursor()
    
    # write query
    query = """ INSERT INTO public.userlistai(
        userid, dob, sex, runningex, fivekm, goaldate, mean_rpe, std_rpe)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s); """    
    # fill query with appropriate user ID
    record_to_insert = (user_id, dob, sex, runningex, fivekm, goaldate, mean_rpe, std_rpe)
        
    # execute query with filled parameters
    curr.execute(query, record_to_insert)
    # make changes in database persistent
    conn.commit()
    # close cursor
    curr.close()
    # close connection

    
        
        

        
        
        
        
        
        
            
            
        
        
        