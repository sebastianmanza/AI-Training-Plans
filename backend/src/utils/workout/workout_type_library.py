from math import sqrt

class workout_type_library:

    ## Creates a trio that can be used as a key in the workout dictionary.
    @staticmethod
    def create_trio(x, y, z):
        return (x, y, z)
    
    ## x range is 1 - 7 , y range is 1 -10, z range is 1 - 10
    ## Dictionary that maps trios of (x, y, z) coordinates to workout types.
    workout_dictionary = {
        create_trio(2.5, 4, 5.5): "ET",
        create_trio(2, 3, 4.5): "Recovery",
        create_trio(4, 6, 3): "Kenyan",
        create_trio(2.5, 5, 9): "Long",
        create_trio(4.5, 7, 4.5): "Threshold",
        create_trio(5, 6, 4): "Fartlek",
        create_trio(5.5, 8, 3.5): "Race Pace Interval",
        create_trio(6.5, 2, .5): "Strides",
        create_trio(7, 3, .5): "Hill Sprints",
        create_trio(7, 6, .5): "Flat Sprints",
        create_trio(6, 10, 3): "Time Trial"
    }

    ## Returns a workout type based on the given x and y coordinates.
    @staticmethod
    def get_workout_type(x, y, z):
        distance = 100
        final_trio = workout_type_library.create_trio(0, 0, 0)
        for trio in workout_type_library.workout_dictionary:
            new_distance = sqrt((trio[0] - x) ** 2 + (trio[1] - y) ** 2 + (trio[2] - z) ** 2)
            if new_distance < distance:
                distance = new_distance
                final_trio = trio

        if final_trio == (0, 0, 0):
            raise ValueError("No matching workout type found for the given coordinates.")
        
        return workout_type_library.workout_dictionary[final_trio]
    
    ## Returns the closest pair of coordinates for a given workout type.
    def get_workout_type_coordinates(x, y, z):
        distance = 100
        final_trio = workout_type_library.create_trio(0, 0, 0)
        for trio in workout_type_library.workout_dictionary:
            new_distance = sqrt((trio[0] - x) ** 2 + (trio[1] - y) ** 2 + (trio[2] - z) ** 2)
            if new_distance < distance:
                distance = new_distance
                final_trio = trio

        if final_trio == (0, 0, 0):
            raise ValueError("No matching workout type found for the given coordinates.")
        
        return final_trio


    def get_workout_difference(x, y, z):
        workout_trio = workout_type_library.get_workout_type_coordinates(x, y, z)
        stimulus_mod = x - workout_trio[0]
        RPE_mod = y - workout_trio[1]
        distance_mod = z - workout_trio[2]
        real_difference = workout_type_library.create_trio(stimulus_mod, RPE_mod, distance_mod)
        return real_difference
        
# Example usage    
print(workout_type_library.get_workout_type(7.3, 4, 1))  #Hill Sprints
print(workout_type_library.get_workout_type_coordinates(7.3, 4, 1))  #ET (7, 3, .5)
print(workout_type_library.get_workout_difference(7.3, 4, 1))  # (.3, 1, .5)

