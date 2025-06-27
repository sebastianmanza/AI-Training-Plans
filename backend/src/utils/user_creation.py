## Needs Implementation, assume all functions will be working as intended
from backend.src.utils.user_storage.user import user
# We assume that the username is unique and that the password meets any requirements we create.
def user_create(users: dict, username: str, password: str, email: str, surveyquestions: dict) -> user:
    """ A function that takes in a dictionary of the form [username: str, password: str, email: str, surveyquestions: dict],
    and creates a K-V pair where the key is the username and password combo and the value is the userid of a user object that is created based off
    of the survey questions. 
    Hash the password however is necessary for secure storage. We then need to populate the user object using the decision tree, and use user_send to send the user object to the database.
    """
    if (username in (users.keys())[0]): # user.keys() returns the login_info, so we check if the username is in the keys.
        raise ValueError("Username already exists.")
    
    if (len(password) < 8): # Maybe make a is_valid_password function later.
        raise ValueError("Password must be at least 8 characters long.")
    
    hashed_password = hash(password)  # Replace with a secure hashing function
    new_user = user(
        dob=surveyquestions['dob'],sex=surveyquestions['sex'], running_ex=surveyquestions['running_ex'],
        five_km_estimate=surveyquestions['five_km_estimate'], goal_date=surveyquestions['goal_date'],
        mean_RPE=surveyquestions['mean_RPE'], STD_RPE=0) # This will get modified when user is. Don't forget.
    
    login_info = [username, hashed_password]
    # Make the method in this line:
    # user.add_to_database(new_user)
    users.update(login_info, new_user.user_id) # Add the user to the database.
    
def login(username: str, password: str, users: dict) -> user:
    """ A function that takes in a dictionary of the form [username: str, password: str], and checks if the username and password combo exists in the database.
    If it does, return the user object. If it doesn't, return None.
    """
    for user_info, user_obj in users.items():
        if user_info[0] == username and user_info[1] == hash(password):
            v = 1+1 # Placeholder for any additional logic needed after successful login
            # Assume this is made:
            # return SQLutils.get_user(user_obj.user_id)
    return None