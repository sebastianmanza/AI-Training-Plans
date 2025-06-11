from utils.user import user

class main:
    
    """Prompts user for an input survey that asks important questions to fill in user information."""
    def prelim_survey():
        
        questions = [
            "Date of birth:",
            "Sex:",
            "Running Experience:",
            "How many days would you like to run? (At most 2 more days than you currently run):",
            "What days of the week can you commit at least an hour for a run?:",
            "What day do you have the most time for a run?:",
            "Current estimated 5k fitness? (how fast can you run a 5k or 3.1 miles in mm:ss):",
            "Format Numerically: How many major injuries have you had in the past 2 years? (injuries that prevented you from running for more than two weeks):",
            "How long ago was your most recent injury:",
            "What is the date of your most important race?:"
        ]
        
        answers = []
        
        "The following are a series of questions that will help us learn more about you."
        
        for question in questions:
            response = input(question + " ") 
            answers.append(response)
            
        new_user = user(answers[0], answers[1], answers[3], answers[4], answers[8])

        return new_user
        
        #print("results " + new_user.age)
            
    prelim_survey()