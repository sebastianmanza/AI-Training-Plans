from backend.src.utils.user_storage import day_plan, month_plan, week_plan
from backend.src.utils.workout.workout_type_library import create_trio
def txt_to_database(filename, database):
    filereader = open(filename)
    """Expect files in format: 
        total_mileage
        goal_stimuli
        expected_rpe"""
    
    # Initialize an empty array that will store the months
    month_ID = 0
    months = []
    
    # Populate a single object in the array
    while not filereader.readline().strip() == "ENDOFMONTHS":
        month_ID += 1
        cycle = filereader.readline().strip()
        month = month_plan(
            month_id=month_ID,
            cycle=cycle)
        months[month_ID] = month
        
    month_ID = 0
    week_ID = 0
    weeks = []
    
    # Populate all week objects in the array
    while not filereader.readline().strip() == "ENDOFWEEKS":
        while not filereader.readline().strip() == "":
            cycle = filereader.readline().strip()
        
        week = week_plan(
                cycle = cycle,
                month_ID = month_ID)
        
        weeks[week_ID] = week
    
        # Add weeks to be children of the month
        week_ID+=1
        if week_ID % 4 == 0:
            months[month_ID].add_weeks(weeks[(week_ID - 4):week_ID])
            month_ID += 1
            
    
    # Note new line is needed at start of file
    week_ID = 0
    days = []
    day_ID = 0
    while not filereader.readline().strip() == "ENDOFDAYS":
        while not filereader.readline().strip() == "":
            # Read the first line for total_mileage
            total_mileage = int(filereader.readline().strip())
        
            # Read the second line for goal_stimuli
            stimuli = filereader.readline().strip().split(sep = ",")
            
            x1, y1, z1 = stimuli[0].split(sep = ":")
            stim1trio = create_trio(x1, y1, z1)
            workout = []
            workout.append(stim1trio)
            
            if stimuli.length > 1:
                x2, y2, z2 = stimuli[1].split(sep = ":")
                stim2trio = create_trio(x2, y2, z2)
                workout.append(stim2trio)
                
        
            # Read the third line for expected_rpe
            expected_rpe = int(filereader.readline().strip())
        
            
        day = day_plan(
            total_mileage=total_mileage,
            workouts=workout,
            expected_rpe=expected_rpe,
            week_id=week_ID
        )
        
        # Add days to the working array (to be added to its week parent), and the database
        days[day_ID] = day
        database.day.put(day)
        
        day_ID+=1

        if day_ID % 7 == 0:
            week_ID += 1

        
    ### Fill in the necessary information for the week, and add day children to the week
    
    week_ID = 0
    for week in weeks:
        day_children = days[(week_ID * 7): (week_ID + 1 * 7)]
        week.add_days(day_children)
        
        weekly_total_mileage = 0
        weekly_stimuli = 0
        weekly_RPE = 0
        weekly_length = 0
        weekly_expected_RPE = 0
        
        for day in day_children:
           
            weekly_total_mileage += day.total_mileage
            x, y, z = day.goal_stimuli
            weekly_stimuli += x
            weekly_RPE += y
            weekly_length += z
            weekly_expected_RPE += day.expected_rpe
            
        week.total_mileage = weekly_total_mileage
        week.goal_stimuli = create_trio(weekly_stimuli, weekly_RPE, weekly_length)
        week.expected_rpe = weekly_expected_RPE

    
    month_ID = 0
    for month in months:
        week_children = weeks[(month_ID * 4): ((month_ID + 1) * 4)]
        month.add_weeks(week_children)
        
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
            
        month.total_mileage = monthly_total_mileage
        month.goal_stimuli = create_trio(monthly_stimuli, monthly_RPE, monthly_length)
        month.expected_rpe = monthly_expected_RPE
        
    for mo in months:
        database.month.put(mo)
    
    for we in weeks:
        database.week.put(we)
    