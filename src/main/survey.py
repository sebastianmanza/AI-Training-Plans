from utils.user import user

class main:
    
    
    def prelim_survey():
        
        questions = [
            "Date of birth",
            "Sex",
            "Running Experience",
            "How many days would you like to run? (At most 2 more days than you currently run)",
            "What days of the week can you commit at least an hour for a run?",
            "What day do you have the most time for a run",
            "Current estimated 5k fitness? (how fast can you run a 5k or 3.1 miles in mm:ss)",
            "Format Numerically: How many major injuries have you had in the past 2 years? (injuries that prevented you from running for more than two weeks).",
            "How long ago was your most recent injury"   
        ]
        
        answers = []
        
        for question in questions:
            response = input(question + " ") 
            answers.append(response)
            
        print("\n --Results -- ")
        for i, question in enumerate(questions):
            (f" {question}: {answers[i]}")
            
        new_user = user(answers[0], answers[1], answers[3], answers[4], answers[8])
        
        print("results " + new_user.age)
            
    prelim_survey()