import sys
import os

# Dynamically find the root directory containing the 'backend' folder
current_dir = os.path.dirname(__file__)
while not os.path.exists(os.path.join(current_dir, "backend")):
    current_dir = os.path.dirname(current_dir)
    if current_dir == "/":  # Stop if we reach the root of the filesystem
        raise RuntimeError("Could not find 'backend' folder in the directory hierarchy.")

# Add the root directory to the Python path
sys.path.append(current_dir)

from backend.src.utils.user_storage.day_plan import day_plan
from backend.src.utils.user_storage.month_plan import month_plan
from backend.src.utils.user_storage.week_plan import week_plan
from backend.src.utils.user_storage.training_database import training_database
from backend.src.utils.workout.workout_database import workout_database

def txt_to_database(filename, database):
    filereader = open(filename)
    """Expect files in format: 
        total_mileage
        goal_stimuli
        expected_rpe"""
    cur_string = ""
    phase = 0
    
# Initialize an empty array that will store the monthsm
    month_ID = 0
    months = []
    
    while cur_string != "ENDOFFILE":
        cur_string = filereader.readline().strip()
        if phase == 0:
            # Check that months is not done
            if cur_string == "ENDOFMONTHS":
                phase = 1 # week phase
                month_ID = 0
                week_ID = 0
                weeks = []
                continue
            
            
            # Read the first line for the cycle
            if cur_string != "":
                cycle = cur_string
                # print(cycle)
        
                # Create the month plan. Note that month_ID is 0 indexed and ordered
                month = month_plan(
                    month_id=month_ID,
                    cycle=cycle)
                months.append(month)
        
                month_ID += 1
        
        # print(months[0].month_id)
            
        elif phase == 1:
            
            # Check that weeks is not done
            if cur_string == "ENDOFWEEKS":
                day_phase = 0
                week_ID = 0
                days = []
                day_ID = 0
                phase = 2
                continue
            
            if cur_string != "":
                cycle = cur_string
                # print(cycle)
                
                week = week_plan(
                    cycle = cycle,
                    month_id = month_ID)
        
                weeks.append(week)
    
                # Add weeks to be children of the month
                week_ID += 1
                if week_ID % 4 == 0:
                    # for we in weeks[(week_ID - 4):week_ID]:
                    #     print(month_ID)
                    #     months[month_ID].weeks.append(we)
                    month_ID += 1
            
        elif phase == 2:
            # read the days
            
            if cur_string == "" or cur_string == "ENDOFFILE":
                continue
            
            if day_phase == 0:
                # Read the first line for total_mileage
                total_mileage = float(cur_string)
                day_phase = 1
            elif day_phase == 1:
                # Read the second line for goal_stimuli
                stimuli = cur_string.split(sep = ",")
            
                x1, y1, z1 = [float(value) for value in stimuli[0].split(sep = "/")]
                stim1trio = workout_database.create_trio(x1, y1, z1)
                workout = []
                workout.append(stim1trio)
                
                # If there are multiple stimuli, read the second one (currently not working for > 2)
                if len(stimuli) > 1:
                    x2, y2, z2 = [float(value) for value in stimuli[1].split(sep = "/")]
                    stim2trio = workout_database.create_trio(x2, y2, z2)
                    workout.append(stim2trio)
                    
                day_phase = 2
            elif day_phase == 2:
                expected_rpe = float(cur_string)
                day_phase = 0
                
                day = day_plan(
                    total_mileage=total_mileage,
                    workouts=workout,
                    expected_rpe=expected_rpe,
                    week_id=week_ID
                )
        
                # Add days to the working array (to be added to its week parent), and the database
                days.append(day)
                database.day.put(day)
        
                day_ID += 1

                if day_ID % 7 == 0:
                    week_ID += 1


    ### Fill in the necessary information for the week, and add day children to the week   
    week_ID = 0
    
    for week in weeks:
        # Find the sublist of days belonging to the week
        end_index = min((week_ID + 1) * 7, len(days))  # Ensure we don't go out of bounds
        day_children = days[(week_ID * 7): end_index]
        week.days = day_children
        
        weekly_total_mileage = 0
        weekly_stimuli = 0
        weekly_RPE = 0
        weekly_length = 0
        weekly_expected_RPE = 0
        
        # Calculate weekly totals based on its day children
        for day in day_children:
           
            weekly_total_mileage += day.total_mileage
            x, y, z = day.goal_stimuli
            weekly_stimuli += x
            weekly_RPE += y
            weekly_length += z
            weekly_expected_RPE += day.expected_rpe
            
        weekly_stimuli = round((weekly_stimuli / len(day_children) if day_children else 0), 1)
        weekly_RPE = round((weekly_RPE / len(day_children) if day_children else 0), 1)
        weekly_length = round((weekly_length / len(day_children) if day_children else 0), 1)
        
        week.total_mileage = weekly_total_mileage
        week.goal_stimuli = workout_database.create_trio(weekly_stimuli, weekly_RPE, weekly_length)
        week.expected_rpe = weekly_expected_RPE
        week_ID += 1

    
    month_ID = 0
    for month in months:
        end_index = min((month_ID + 1) * 4, len(weeks))  # Ensure we don't go out of bounds
        week_children = weeks[(month_ID * 4): end_index]
        month.weeks = week_children
        
        monthly_total_mileage = 0
        monthly_stimuli = 0
        monthly_RPE = 0
        monthly_length = 0
        monthly_expected_RPE = 0
        
        for week in week_children:
            monthly_total_mileage += week.total_mileage
            x, y, z = week.goal_stimuli
            monthly_stimuli += x
            monthly_RPE += y
            monthly_length += z
            monthly_expected_RPE += week.expected_rpe
            
        # Update the month with the calculated totals
        monthly_stimuli = round((monthly_stimuli / len(week_children) if week_children else 0), 1)
        monthly_RPE = round((monthly_RPE / len(week_children) if week_children else 0), 1)
        monthly_length = round((monthly_length / len(week_children) if week_children else 0), 1)
        
        
        month.total_mileage = monthly_total_mileage
        month.goal_stimuli = workout_database.create_trio(monthly_stimuli, monthly_RPE, monthly_length)
        month.expected_rpe = monthly_expected_RPE
        month_ID += 1
        
    for mo in months:
        database.month.put(mo)
    
    for we in weeks:
        database.week.put(we)
    # Close the file reader
    filereader.close()
 
# Example usage
txt_to_database("backend/data/raw/training_plan_test.txt", database=training_database)