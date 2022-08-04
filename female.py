# inherit everything from Human class into female
from human import Human

# create a male class
class Female(Human): # write the name of the class in () - (parent class) to inherit
    # parent class - base class - super class

    def __init__(self):
        # need to let it know to inherit everything from parent class (Animal)
        super().__init__() # super is used to inherit everything from base class
        self.hair = bool
        self.ears = 2
        self.walk = True

    def shopping(self):
        return "Shopping makes me happy!"

    def __work(self): # Private method
        return "working hard..."

    def _gym(self): # Protected method
        return "Regular exercise benefits your health"

    # create an object of female class
female_object = Female()

#print(female_object.eat())
#print(female_object.shopping())