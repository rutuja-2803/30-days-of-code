class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age=0
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age=initialAge
    def amIOld(self):
        if age<13:
            print("You are young.")
        elif age>=13 and age<18:
            print("You are a teenager.")
        else:
            print("You are old.") 
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age+=1
        

t = int(input())