from utils.user import user
import psycopg2

class main:
    

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
        
        try:
            # establish connection with user list database
            conn = psycopg2.connect(database = "UserList",
                                    user = "postgres",
                                    host = "localhost",
                                    password = "Control1500#",
                                    port = "5432")

            # open cursor to perform sql queries
            curr = conn.cursor()

            database_query = (""" INSERT INTO public.userlistai(dob, sex, runningex, fivekm, goaldate) VALUES (%s,%s,%s,%s,%s); """)
            record_to_insert = (answers[0], answers[1], answers[3], answers[4], answers[8])
            curr.execute(database_query, record_to_insert)

            # make changes in database persistent
            conn.commit()

            # close cursor
            curr.close()
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            # return None

        print("results " + new_user.age)

            
    prelim_survey()