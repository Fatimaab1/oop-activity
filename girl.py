# inherit everything from Female class into girl
from female import Female

# create a female class
class Girl(Female): # write the name of the class in () - (parent class) to inherit
    # parent class - base class - super class

    def __init__(self):
        # need to let it know to inherit everything from parent class (Animal)
        super().__init__() # super is used to inherit everything from base class
        self.legs = bool
        self.fingers = 5
        self.walk = True

    def school(self):
        return "School is fun!"

    def ballet(self):
        return "I enjoy ballet"

    def play(self):
        return "I like to play outside"

    # create an object of female class
girl_object = Girl()

print(girl_object._gym())
print(girl_object.shopping())