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
def send_month_cycle(new_user, username, password):
    
    conn = init_db(username, password)
    # open cursor to perform sql queries
    curr = conn.cursor()
    
    while new_user.month_history:
        
        pres = new_user.month_history.pop()
        # write query
        query = """ INSERT INTO public.month_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, month_id, past_month, complete_mileage)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """    
        # fill query with appropriate user ID
    
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (pres.user_id, pres.total_mileage, pres.goal_stimuli, pres.cycle, pres.expected_rpe, pres.real_rpe,
                            pres.percent_completion, 1, True, pres.completed_mileage)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        
    while new_user.month_furture:
        
        fut = new_user.month_future.pop()
        # write query
        query = """ INSERT INTO public.month_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, month_id, past_month, complete_mileage)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """  
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (fut.user_id, fut.total_mileage, fut.goal_stimuli, fut.cycle, fut.expected_rpe, fut.real_rpe,
                            fut.percent_completion, 1, False, fut.completed_mileage)
        
        # execute query with filled parameters
        curr.execute(query, record_to_insert)
  
    # make changes in database persistent
    conn.commit()
        
    # close cursor
    curr.close()
    

# populate week cycle user infomation within SQL database
def send_week_cycle(new_user, username, password):
    
    conn = init_db(username, password)
    # open cursor to perform sql queries
    curr = conn.cursor()
    
    while new_user.week_history:
        
        pres = new_user.week_history.pop()
        

        # write query
        query = """ INSERT INTO public.week_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, week_id, past_week, complete_mileage, month_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """   
        # fill query with appropriate user ID
    
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (pres.user_id, pres.total_mileage, pres.goal_stimuli, pres.cycle, pres.expected_rpe, pres.real_rpe, 
                            pres.percent_completion, 1, True, pres.completed_mileage, 1)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        
    while new_user.week_future:
        
        fut = new_user.week_future.pop()
        
        # write query
        query = """ INSERT INTO public.week_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, week_id, past_week, complete_mileage, month_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """   
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (fut.user_id, fut.total_mileage, fut.goal_stimuli, fut.cycle, fut.expected_rpe, fut.real_rpe,  
                            fut.completed_mileage, fut.percent_completion, 1, False, 1)
        
        # execute query with filled parameters
        curr.execute(query, record_to_insert)
  
    # make changes in database persistent
    conn.commit()
        
    # close cursor
    curr.close()
    
    
# populate day cycle user infomation within SQL database
def send_day_cycle(new_user, username, password):
    
    conn = init_db(username, password)
    # open cursor to perform sql queries
    curr = conn.cursor()
    
    while new_user.day_history:
        
        pres = new_user.day_history.pop()
        

        # write query
        query = """ INSERT INTO public.day_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, past_day, complete_mileage, week_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """   
        # fill query with appropriate user ID
    
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (pres.user_id, pres.total_mileage, pres.goal_stimuli, pres.cycle, pres.expected_rpe, pres.real_rpe,
                            pres.percent_completion, True, pres.completed_mileage, 1)

        # execute query with filled parameters
        curr.execute(query, record_to_insert)
        
    while new_user.day_future:
        
        fut = new_user.day_future.pop()
        
        # write query
        query = """ INSERT INTO public.day_cycle(
            user_id, total_mileage, goal_stimuli, cycle, expected_rpe, real_rpe, complete_score, past_day, complete_mileage, week_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """     
        # 1 is a placeholder (too lazy to change shit)
        record_to_insert = (fut.user_id, fut.total_mileage, fut.goal_stimuli, fut.cycle, fut.expected_rpe, fut.real_rpe,
                            fut.percent_completion, 1, True, fut.completed_mileage, 1)
        
        # execute query with filled parameters
        curr.execute(query, record_to_insert)
  
    # make changes in database persistent
    conn.commit()
        
    # close cursor
    curr.close()
    



# testing     

new_user = user("16", "F", "five", "4", 6, 8, 8)

send_user_info(new_user, DB_CREDENTIALS["DB_USERNAME"], DB_CREDENTIALS["DB_PASSWORD"])

pres = new_user.month_history.pop()



    
    
