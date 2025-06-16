import psycopg2
from backend.src.utils.SQLutils.database_connect import db_insert
from backend.src.utils.user_storage.user import user
from backend.src.main.survey import main 

# Sends user information to the database.
def send_user_info(new_user, SQL_user, password):
    #prepare query 
    db_query = """ INSERT INTO public.userlistai(dob, sex, runningex, fivekm, goaldate) VALUES (%s,%s,%s,%s,%s); """
    
    # for furture use
    # param_count = db_query.count("%s")
    # Initialize the connection with the database
    db_insert(SQL_user, password, db_query, new_user.age, new_user.five_km_estimate, new_user.goal_date, new_user.running_ex,
                    new_user.mean_RPE, new_user.STD_RPE)
    
    
    
    send_user_info(main.prelim_survey(), "postgres", "Control1500#")
    
    
    
    
    

<<<<<<< HEAD
    
    
=======
    # Create a new user object

    user = user()
>>>>>>> 9f016e9e77f3080a85a8179aee0adf8342d69c4e
