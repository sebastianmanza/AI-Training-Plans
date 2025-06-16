from math import sqrt

class workout_type_library:

    ## Creates a pair that can be used as a key in the workout dictionary.
    @staticmethod
    def create_pair(x, y):
        return (x, y)
    
    ## x range is 1 - 7 , y range is 1 -10
    ## Dictionary that maps pairs of (x, y) coordinates to workout types.
    workout_dictionary = {
        create_pair(2.5, 4): "ET",
        create_pair(2, 3): "Recovery",
        create_pair(4, 6): "Kenyan",
        create_pair(2.5, 5): "Long",
        create_pair(4.5, 7): "Threshold",
        create_pair(5, 6): "Fartlek",
        create_pair(5.5, 8): "Race Pace Interval",
        create_pair(6.5, 2): "Strides",
        create_pair(7, 3): "Hill Sprints",
        create_pair(7, 6): "Flat Sprints",
        create_pair(6, 10): "Time Trial"
    }

    ## Returns a workout type based on the given x and y coordinates.
    @staticmethod
    def get_workout_type(x, y):
        distance = 100
        final_pair = workout_type_library.create_pair(0, 0)
        for pair in workout_type_library.workout_dictionary:
            new_distance = sqrt((pair[0] - x) ** 2 + (pair[1] - y) ** 2)
            if new_distance < distance:
                distance = new_distance
                final_pair = pair

        if final_pair == (0, 0):
            raise ValueError("No matching workout type found for the given coordinates.")
        
        return workout_type_library.workout_dictionary[final_pair]
    
    ## Returns the closest pair of coordinates for a given workout type.
    def get_workout_type_coordinates(x, y):
        distance = 100
        final_pair = workout_type_library.create_pair(0, 0)
        for pair in workout_type_library.workout_dictionary:
            new_distance = sqrt((pair[0] - x) ** 2 + (pair[1] - y) ** 2)
            if new_distance < distance:
                distance = new_distance
                final_pair = pair

        if final_pair == (0, 0):
            raise ValueError("No matching workout type found for the given coordinates.")
        
        return final_pair


    def get_workout_difference(x, y):
        workout_pair = workout_type_library.get_workout_type_coordinates(x, y)
        stimulus_mod = x - workout_pair[0]
        RPE_mod = y - workout_pair[1]
        real_difference = workout_type_library.create_pair(stimulus_mod, RPE_mod)
        return real_difference
        
# Example usage    
print(workout_type_library.get_workout_type(7.3, 4))  #Hill Sprints
print(workout_type_library.get_workout_type_coordinates(7.3, 4))  #ET (7, 3)
print(workout_type_library.get_workout_difference(7.3, 4))  # (.3, 1)

