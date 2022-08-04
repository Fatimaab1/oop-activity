# inherit everything from Male class into boy
from male import Male

# create a boy class
class Boy(Male): # write the name of the class in () - (parent class) to inherit
    # parent class - base class - super class

    def __init__(self):
        # need to let it know to inherit everything from parent class (Animal)
        super().__init__() # super is used to inherit everything from base class
        self.facial_hair = bool
        self.hair = True
        self.hands = 2

    def school(self):
        return "I enjoy going to school"

    def play(self):
        return "I like playing with my friends"

    def football(self):
        return "Football is my favourite sport"

    # create an object of boy class
boy_object = Boy()

#print(boy_object.work())
#print(boy_object.school())