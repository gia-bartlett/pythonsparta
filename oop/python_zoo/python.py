from snake import Snake
# importing the attributes from Snake class in snake file

class Python(Snake):  # name class (taking attributes from Snake as well)

    def __init__(self):  # define initial variables for all pythons
        super().__init__() # inheriting initial variables from Animal (super refers to parent)
        self.venom = False # pythons don't produce venom
        self.constrict = True # pythons constrict their prey

    def swim(self):
        print("just keep swimming...just keep swimming")

    def camouflaged(self):
        print("sneaky")



burmese = Python()

print(burmese.swim()) # just keep swimming...just keep swimming
