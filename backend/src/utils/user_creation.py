## Needs Implementation, assume all functions will be working as intended

def user_create(dict):
    """ A function that takes in a dictionary of the form [username: str, password: str, email: str, surveyquestions: dict],
    and creates a K-V pair where the key is the username and password combo and the value is the userid of a user object that is created based off
    of the survey questions. 
    Hash the password however is necessary for secure storage. We then need to populate the user object using the decision tree, and use user_send to send the user object to the database.
    """
    
def login(dict) -> user:
    """ A function that takes in a dictionary of the form [username: str, password: str], and checks if the username and password combo exists in the database.
    If it does, return the user object. If it doesn't, return None.
    """
