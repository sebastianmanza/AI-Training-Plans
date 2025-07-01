from backend.src.utils.user_storage.user import user

USERNAME_LOC, PASSWORD_LOC = 0, 1
PASS_LEN_REQ = 8


def user_create(users: dict, username: str, password: str, email: str, surveyquestions: dict) -> user:
    """ A function that takes in a dictionary of the form [username: str, password: str, email: str, surveyquestions: dict],
    and creates a K-V pair where the key is the username and password combo and the value is the userid of a user object that is created based off
    of the survey questions. 
    Hash the password however is necessary for secure storage. We then need to populate the user object using the decision tree, and use user_send to send the user object to the database.
    """
    if (username in (users.keys())[USERNAME_LOC]):  # user.keys() returns the login_info, so we check if the username is in the keys.
        raise ValueError("Username already exists.")

    if (len(password) < PASS_LEN_REQ):  # Maybe make a is_valid_password function later.
        raise ValueError("Password must be at least 8 characters long.")

    hashed_password = hash(password)  # Replace with a secure hashing function
    new_user = user(
        dob=surveyquestions['dob'], sex=surveyquestions['sex'], running_ex=surveyquestions['running_ex'],
        five_km_estimate=surveyquestions['five_km_estimate'], goal_date=surveyquestions['goal_date'],
        # This will get modified when user is. Don't forget.
        mean_RPE=surveyquestions['mean_RPE'], STD_RPE=0)

    login_info = [username, hashed_password]
    # Make the method in this line:
    # user.add_to_database(new_user)
    # When a new user is created user.py handles creating a user id.
    users.update(login_info, new_user.user_id)  # Add the user to the database.


def login(username: str, password: str, users: dict) -> user:
    """ A function that takes in a dictionary of the form [username: str, password: str], and checks if the username and password combo exists in the database.
    If it does, return the user object. If it doesn't, return None.
    """
    for user_info, user_obj in users.items():
        if user_info[USERNAME_LOC] == username and user_info[PASSWORD_LOC] == hash(password):
            v = 1+1  # Placeholder for any additional logic needed after successful login
            # Assume this is made:
            # return SQLutils.get_user(user_obj.user_id)
    return None
