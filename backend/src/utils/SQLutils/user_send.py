import psycopg2
from backend.src.utils.SQLutils.database_connect import db_insert, db_update
from backend.src.utils.user_storage.user import user
from backend.src.utils.SQLutils.database_connect import init_db
from backend.src.utils.SQLutils.config import DB_CREDENTIALS



# Sends user information to the database.
def send_user_info(new_user, username, password):
    
    try:
        # Initialize the connection with the database
        tryconn = init_db(username, password)
        # open cursor to perform sql queries
        curr = tryconn.cursor()
        #check to see that the user does not already exist
        db_query = """ SELECT * FROM public.userlistai WHERE userid = %s """
        record_to_insert = (new_user.user_id)
        
         # execute query with filled parameters
        curr.execute(db_query, record_to_insert)
        # make changes in database persistent
        tryconn.commit()
        # close cursor
        curr.close()
        # close connection
        tryconn.close()
        
        # now update the information of the existing user within the SQL database
        db_update(username, password, new_user.userid, new_user.age, new_user.sex, new_user.five_km_estimate, new_user.goal_date, 
                    new_user.running_ex, new_user.mean_RPE, new_user.STD_RPE)
        
    except Exception:
        
        # inserts as a new row in the database if user does not exist already
        db_insert(username, password, new_user.age, new_user.sex, new_user.five_km_estimate, new_user.goal_date, new_user.running_ex,
                    new_user.mean_RPE, new_user.STD_RPE)
  

# populate month cycle user infomation within SQL database
def send_month_cycle(user, username, password):
    
    conn = init_db(username, password)
    # open cursor to perform sql queries
    curr = conn.cursor()
    
    while new_user.month_history:
        curr = new_user.month_history.pop()

        # write query
        query = """ INSERT INTO public.month_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, month_id, past_month, complete_mileage)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """    
        # fill query with appropriate user ID
    
    
        record_to_insert = (curr.user_id, curr.goal_stim, curr.runningex, curr.fivekm, goaldate, mean_rpe, std_rpe)

        # execute query with filled parameters
        # curr.execute(query, record_to_insert)
        # make changes in database persistent
    
    conn.commit()
    # close cursor
    curr.close()
    



# testing     

new_user = user("16", "F", "five", "4", 6, 8, 8)

send_user_info(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])





    
    