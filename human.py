# Create Human class
# syntax class name:

class Human:
    # __init__ to declare class attribues (to initialise a class)

    def __init__(self): # self refers to current class
        self.eyes = True
        self.hands = 2
        self.alive = True

    def sleep(self):
        return "Humans need between 7 + hours of sleep a night"

    def eat(self):
        return "eat if you like to stay alive.. and eat healthy."

    def move(self):
        return "The human body was designed to move"


# create an object of the class before using it
human_object = Human()
#print(human_object.move())