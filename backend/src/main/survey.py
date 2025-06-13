from backend.src.utils.user_storage import day_plan
from backend.src.utils.user_storage import user, week_plan
from backend.src.utils.user_storage.month_plan import month_plan
import psycopg2

class main:
    
    """This is the main class that will run the preliminary survey for the user and store it in the database."""
    def prelim_survey():
        
        # Preliminary questions that will make up the users initial info.
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

        # print("results " + new_user.age)

            
    # prelim_survey()
    def daily_post_run_survey():
        """This is the post run survey that will be used to gather data from the user after each run."""
        questions = [
            "How would you rate this running using the RPE metric? (scale of 1-10):",
            "Was your daily mileage within the prescribed range:",
            "If not what was your daily mileage?:",
            "Was your average pace within the prescribed pace range:",
            "If not what was your average pace?:",
            "Was your rest in the prescribed range?:",
            "If not what was your rest?:",
            "Did you complete a lift today?:"
        ]
        
        answers = []
        for question in questions:
            response = input(question + " ")
            answers.append(response)

        new_day = day_plan(
            real_rpe=int(answers[0]),
            #None should be mileage from the expected plan
            total_mileage=int(answers[2]) if answers[1].lower() == "no" else None,
            #None should be the expected pace from the expected plan
            pace=int(answers[4]) if answers[3].lower() == "no" else None,
            #None should be the expected rest from the expected plan
            rest=int(answers[6]) if answers[5].lower() == "no" else None,
            lift=answers[7].lower() == "yes",
        )
     
        
        # Here you would typically store the answers in a database or process them further.
        print("Post-run survey completed. Thank you for your feedback!")

    def post_week_survey():
        """This is the post week survey that will be used to gather data from the user after each week."""
        questions = [
            "How would you rate this weeks worth of effort using the RPE metric? (scale of 1-10):"
        ]
        
        answers = []
        for question in questions:
            response = input(question + " ")
            answers.append(response)
        
        new_week = week_plan(
            real_rpe=int(answers[0]),
        )

        # Here you would typically store the answers in a database or process them further.
        print("Post-week survey completed. Thank you for your feedback!")

    def post_month_survey():
        """This is the post month survey that will be used to gather data from the user after each month."""
        questions = [
            "How would you rate this months worth of effort using the RPE metric? (scale of 1-10):"
        ]
        
        answers = []
        for question in questions:
            response = input(question + " ")
            answers.append(response)
        
        new_month = month_plan(
            real_rpe=int(answers[0]),
        )

        # Here you would typically store the answers in a database or process them further.
        print("Post-month survey completed. Thank you for your feedback!")
    # prelim_survey()