# inherit everything from Human class into male
from human import Human

# create a male class
class Male(Human): # write the name of the class in () - (parent class) to inherit
    # parent class - base class - super class

    def __init__(self):
        # need to let it know to inherit everything from parent class (Animal)
        super().__init__() # super is used to inherit everything from base class
        self.beard = True
        self.deep_voice = True
        self.nose = True

    def sports(self):
        return "Enjoy playing sport to stay active"

    def work(self):
        return "working hard..."

    def watching_football(self):
        return "Entertainment"

    # create an object of male class
male_object = Male()

#print(male_object.sleep())
#print(male_object.work())