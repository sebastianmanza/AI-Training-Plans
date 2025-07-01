#user needs a variable longest_long_run
#user needs more injury inputs
#we need to create a way to pull running plans from the folder
#we need a way to create key/value pairs for running folder
class decision_tree:
    def __init__(self, user):
      self.user = user
    
    def get_decision_tree(self):
        #checks if user age is less than or equal to 15
        if self.user.age <= 15:
            #user is 15 or younger
            ##checks if user is male
            if self.user.sex == "male":
                #user is 15 or younger
                ##user is male
                ##checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is 15 or younger
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 2 miles
                        if self.user.longest_long_run <= 2:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 3 - 4 miles
                        elif self.user.longest_long_run <= 4:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 5 - 6 miles
                        elif self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is 15 or younger
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                            #user is 15 or younger
                            ##user is male
                            ###user is a beginner runner
                            ####user has been injured 1 - 2 times
                            ######user most recent injury is 0 - 3 months ago
                            ######checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is 15 or under
                    ##user is male
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                #user is 15 or younger
                ##user is male
                ###user is an intermediate or advanced runner
                else:
                    #user is 15 or younger
                    ##user is male
                    ###user is an intermediate or advanced runner
                    ####checks if user has no injuries
                    if self.user.injury == 0:
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 4 miles
                        if self.user.longest_long_run <= 4:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 4 - 6 miles
                        elif self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is 15 or younger
                    ##user is male
                    ###user is an intermediate or advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is 15 or younger
                    ##user is male
                    ###user is an intermediate or advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 miles+
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is male
                        ###user is an intermediate or advanced runner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is male
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
            #user is 15 or younger
            ##user is female or other
            else:
                #user is 15 or younger
                ##user is female or other
                ###checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is 15 or younger
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has no injuries
                    if self.user.injury == 0:
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 2 miles
                        if self.user.longest_long_run <= 2:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 3 - 4 miles
                        elif self.user.longest_long_run <= 4:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 5 - 6 miles
                        elif self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is 15 or younger
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is 15 or younger
                    ##user is female or other
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 2 miles
                            if self.user.longest_long_run <= 2:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 3 - 4 miles
                            elif self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6+ miles
                            else:
                                #return training_plan
                                return -1
                #user is 15 or under
                ##user is female or other
                ###user is an intermediate or advanced runner        
                else:
                    #user is 15 or under
                    ##user is female or other
                    ###user is an intermediate or advanced runner
                    ####checks if user has no injuries
                    if self.user.injury == 0:
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 4 miles
                        if self.user.longest_long_run <= 4:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 4 - 6 miles
                        elif self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is 15 or under
                    ##user is female or other
                    ###user is an intermediate or advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is 15 or under
                    ##user is female or other
                    ###user is an intermediate or advanced runner
                    ####user has been injured 3+ times
                    else:
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is 15 or younger
                        ##user is female or other
                        ###user is an intermediate or advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 4 miles
                            if self.user.longest_long_run <= 4:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 6 miles
                            elif self.user.longest_long_run <= 6:
                                #return training_plan
                                return -1
                            #user is 15 or under
                            ##user is female or other
                            ###user is an intermediate or advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
        #checks if user age is less than or equal to 25
        elif self.user.age <= 25:
            #user is between 15 and 25
            ##checks if user is male
            if self.user.sex == "male":
                #user is between 15 and 25
                ##user is male
                ###checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is between 15 and 25
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has no injuries
                    if self.user.injury == 0:
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 5 miles
                        if self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 15 and 25
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 15 and 25
                    ##user is male
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12- 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 15 and 25
                ##user is male
                ###check if user is an intermediate runner
                elif self.user.running_ex == "intermediate":
                    #user is between 15 and 25
                    ##user is male
                    ###user is an intermediate runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 6 miles
                        if self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7 - 8 miles
                        elif self.user.longest_long_run <= 8:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9 - 10 miles
                        elif self.user.longest_long_run <= 10:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 11+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 15 and 25
                    ##user is male
                    ###user is an intermediate runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 1 - 2 injuries
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 15 and 25
                    ##user is male
                    ###user is an intermediate runner
                    ####user has 3+ injuries
                    else:
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3  - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12- 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 15 and 25
                ##user is male
                ###user is an advanced runner
                else:
                    #user is between 15 and 25
                    ##user is male
                    ###user is an advanced runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 7 miles
                        if self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10 - 11 miles
                        elif self.user.longest_long_run <= 11:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 11+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 15 and 25
                    ##user is male
                    ###user is an advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 15 and 25
                    ##user is male
                    ###user is an advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
            #user is between 15 and 25
            ##user is female or other
            else:
                #user is between 15 and 25
                ##user is female or other
                ## checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 5 miles
                        if self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 15 and 25
                ##user is female or other
                ###checks if user is an intermediate runner
                elif self.user.running_ex == "intermediate":
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is an intermediate runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 5 miles
                        if self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is an intermediate runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3 - 6 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is an intermediate runner
                    ####user has 3+ injuries
                    else:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 15 and 25
                ##user is female or other
                ###user is an advanced runner
                else:
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is an advanced runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 7 miles
                        if self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10 - 11 miles
                        elif self.user.longest_long_run <= 11:
                            #return training_plan
                            return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 11+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is an advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 1+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 1+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 1+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 1+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 15 and 25
                    ##user is female or other
                    ###user is an advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 1+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 1+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 1+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 15 and 25
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 15 and 25
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 1+ miles
                            else:
                                #return training_plan
                                return -1
        #checks if user age is less than or equal to 40
        elif self.user.age <= 40:
            #user is between 25 and 40
            ##checks if user is male
            if self.user.sex == "male":
                #user is between 25 and 40
                ##user is male
                ###checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is between 25 and 40
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 5 miles
                        if self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 25 and 40
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 25 and 40
                    ##user is male
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 5 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 5 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 5 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 5 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 25 and 40
                ##user is male
                ##checks if user is an intermediate runner
                elif self.user.running_ex == "intermediate":
                    #user is between 25 and 40
                    ##user is male
                    ###user is an intermediate runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 6 miles
                        if self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7 - 8 miles
                        elif self.user.longest_long_run <= 8:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9 - 10 miles
                        elif self.user.longest_long_run <= 10:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 25 and 40
                    ##user is male
                    ###user is an intermediate runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 25 and 40
                    ##user is male
                    ###user is an intermediate runner
                    ####user has 3+ injuries
                    else:
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 25 and 40
                ##user is male
                ###user is an andvanced runner
                else:
                    #user is between 25 and 40
                    ##user is male
                    ###user is an advanced runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 7 miles
                        if self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10 - 11 miles
                        elif self.user.longest_long_run <= 11:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 11+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 25 and 40
                    ##user is male
                    ###user is an advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 25 and 40
                    ##user is male
                    ###user is an advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
            #user is between 25 and 40
            ##user is female or other
            else:
                #user is between 25 and 40
                ##user is female or other
                ###checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 5 miles
                        if self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 25 and 40
                ##user is female or other
                ###checks if user is an intermediate runner
                elif self.user.running_ex == "intermediate":
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is an intermediate runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 6 miles
                        if self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7 - 8 miles
                        elif self.user.longest_long_run <= 8:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9 - 10 miles
                        elif self.user.longest_long_run <= 10:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is an intermediate runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is an intermediate runner
                    ####user has 3+ injuries
                    else:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 25 and 40
                ##user is female or other
                ###user is an advanced runner
                else:
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is an advanced runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 7 miles
                        if self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7 - 8 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9 - 10 miles
                        elif self.user.longest_long_run <= 11:
                            #return training_plan
                            return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 11+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is an advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 25 and 40
                    ##user is female or other
                    ###user is an advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 25 and 40
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 25 and 40
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
        #checks if user age is less than or equal to 55
        elif self.user.age <= 55:
            #user is between 40 and 55
            ##checks if user is male
            if self.user.sex == "male":
                #user is between 40 and 55
                ##user is male
                ###checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is between 40 and 55
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 5 miles
                        if self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 40 and 55
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 40 and 55
                    ##user is male
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 40 and 55
                ##user is male
                ###checks if user is an intermediate runner
                elif self.user.running_ex == "intermediate":
                    #user is between 40 and 55
                    ##user is male
                    ###user is an intermediate runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 6 miles
                        if self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7 - 8 miles
                        elif self.user.longest_long_run <= 8:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9 - 10 miles
                        elif self.user.longest_long_run <= 10:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 40 and 55
                    ##user is male
                    ###user is an intermediate runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 40 and 55
                    ##user is male
                    ###user is an intermediate runner
                    ####user has 3+ injuries
                    else:
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 -12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 40 and 55
                ##user is male
                ###user is an advanced runner
                else:
                    #user is between 40 and 55
                    ##user is male
                    ###user is an advanced runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 7 miles
                        if self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10 - 11 miles
                        elif self.user.longest_long_run <= 11:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 11+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 40 and 55
                    ##user is male
                    ###user is an advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 40 and 55
                    ##user is male
                    ###user is an advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
            #user is between 40 and 55
            ##user is female or other
            else:
                #user is between 40 and 55
                ##user is female or other
                ###checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 5 miles
                        if self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 5 miles
                            if self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 40 and 55
                ##user is female or other
                ###checks if user is an intermediate runner
                elif self.user.running_ex == "intermediate":
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is an intermediate runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 56 miles
                        if self.user.longest_long_run <= 6:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7 - 8 miles
                        elif self.user.longest_long_run <= 8:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 9 - 10 miles
                        elif self.user.longest_long_run <= 10:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is an intermediate runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is an intermediate runner
                    ####user has 3+ injuries
                    else:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6  - 12 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 6 miles
                            if self.user.longest_long_run <= 6:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7 - 8 miles
                            elif self.user.longest_long_run <= 8:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 9 - 10 miles
                            elif self.user.longest_long_run <= 10:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10+ miles
                            else:
                                #return training_plan
                                return -1
                #user is between 40 and 55
                ##user is female or other
                ###user is an advanced runner
                else:
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is an advanced runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 7 miles
                        if self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10 - 11 miles
                        elif self.user.longest_long_run <= 11:
                            #return training_plan
                            return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 11+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is an advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is between 40 and 55
                    ##user is female or other
                    ###user is an advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is between 40 and 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is between 40 and 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
        #user age is over 55
        else:
            #user is over the age of 55
            ##checks if user is male
            if self.user.sex == "male":
               #user is over the age of 55
               ##user is male
               ###checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is over 55
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 3 miles
                        if self.user.longest_long_run <= 3:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 4 - 5 miles
                        elif self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is over 55
                    ##user is male
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is over 55
                    ##user is male
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                #user is over the age of 55
                ##user is male
                ###checks if user is an intermediate runner
                elif self.user.running_ex == "intermediate":
                    #user is over 55
                    ##user is male
                    ###user is an intermediate runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 3 miles
                        if self.user.longest_long_run <= 3:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 4 - 5 miles
                        elif self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is over 55
                    ##user is male
                    ###user is an intermediate runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is over 55
                    ##user is male
                    ###user is an intermediate runner
                    ####user has 3+ injuries
                    else:
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                #user is over the age of 55
                ##user is male
                ###user is an advanced runner
                else:
                    #user is over 55
                    ##user is male
                    ###user is an advanced runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 7 miles
                        if self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 8 - 9 miles
                        elif self.user.longest_long_run <= 9:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 10 - 11 miles
                        elif self.user.longest_long_run <= 11:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 11+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is over 55
                    ##user is male
                    ###user is an advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is over 55
                    ##user is male
                    ###user is an advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is male
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is male
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
            #user is over the age of 55
            ##user is female or other
            else:
                #user is over the age of 55
                ##user is female or other
                ###checks if user is a beginner runner
                if self.user.running_ex == "beginner":
                    #user is over 55
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 3 miles
                        if self.user.longest_long_run <= 3:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 4 - 5 miles
                        elif self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is over 55
                    ##user is female or other
                    ###user is a beginner runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is over 55
                    ##user is female or other
                    ###user is a beginner runner
                    ####user has 3+ injuries
                    else:
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is a beginner runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is a beginner runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                #user is over the age of 55
                ##user is female or other
                ###checks if user is an intermediate runner
                elif self.user.running_ex == "intermediate":
                    #user is over 55
                    ##user is female or other
                    ###user is an intermediate runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 3 miles
                        if self.user.longest_long_run <= 3:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 4 - 5 miles
                        elif self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is over 55
                    ##user is female or other
                    ###user is an intermediate runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is over 55
                    ##user is female or other
                    ###user is an intermediate runner
                    ####user has 3+ injuries
                    else:
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an intermediate runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 3 miles
                            if self.user.longest_long_run <= 3:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 4 - 5 miles
                            elif self.user.longest_long_run <= 5:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 6 - 7 miles
                            elif self.user.longest_long_run <= 7:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an intermediate runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 7+ miles
                            else:
                                #return training_plan
                                return -1
                #user is over the age of 55
                ##user is female or other
                ###user is an advanced runner
                else:
                    #user is over 55
                    ##user is female or other
                    ###user is an advanced runner
                    ####checks if user has 0 injuries
                    if self.user.injury == 0:
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 0 - 3 miles
                        if self.user.longest_long_run <= 3:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 4 - 5 miles
                        elif self.user.longest_long_run <= 5:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 6 - 7 miles
                        elif self.user.longest_long_run <= 7:
                            #return training_plan
                            return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has 0 injuries
                        #####checks if user longest long run is 7+ miles
                        else:
                            #return training_plan
                            return -1
                    #user is over 55
                    ##user is female or other
                    ###user is an advanced runner
                    ####checks if user has 1 - 2 injuries
                    elif self.user.injury < 3:
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 1 - 2 times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 1 - 2 injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                    #user is over 55
                    ##user is female or other
                    ###user is an advanced runner
                    ####user has 3+ injuries
                    else:
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 0 - 3 months ago
                        if self.user.most_recent_injury < 3:
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 0 - 3 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 3 - 6 months ago
                        elif self.user.most_recent_injury < 6:
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 3 - 6 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 6 - 12 months ago
                        elif self.user.most_recent_injury < 12:
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 6 - 12 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1
                        #user is over 55
                        ##user is female or other
                        ###user is an advanced runner
                        ####user has been injured 3+ times
                        #####checks if user most recent injury is 12 - 24 months ago
                        else:
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 0 - 7 miles
                            if self.user.longest_long_run <= 7:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 8 - 9 miles
                            elif self.user.longest_long_run <= 9:
                                #return training_plan
                                 return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 10 - 11 miles
                            elif self.user.longest_long_run <= 11:
                                #return training_plan
                                return -1
                            #user is over 55
                            ##user is female or other
                            ###user is an advanced runner
                            ####user has 3+ injuries
                            #####user most recent injury is 12 - 24 months ago
                            ######checks if user longest long run is 11+ miles
                            else:
                                #return training_plan
                                return -1