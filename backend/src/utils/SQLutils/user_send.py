import psycopg2
from backend.src.utils.SQLutils.database_connect import db_insert
from backend.src.utils.user_storage.user import user
from backend.src.main import survey

"""Sends user information to the database."""
def send_user_info(user_info, SQL_user, password):

    db_query = """ INSERT INTO public.userlistai(dob, sex, runningex, fivekm, goaldate) VALUES (%s,%s,%s,%s,%s); """
    
    survey()
    
    # for furture use
    param_count = db_query.count("%s")
    
    
    # Initialize the connection with the database
    db_insert(SQL_user, password, user_info, db_query)
    

    # Create a new user object
    user = user()
