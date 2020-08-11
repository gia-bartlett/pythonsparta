from reptile import Reptile
# importing the attributes from Reptile class in reptile file

class Snake(Reptile):  # name class (taking attributes from Reptile as well)

    def __init__(self):  # define initial variables for all snakes
        super().__init__() # inheriting initial variables from Animal (super refers to parent)
        self.diurnal = True # reptiles have two eyes
        self.oviparous = True # reptiles lay eggs

    def slither(self):
        print("wigglewiggle")

    def smell(self):
        print("Stick out my tongue...smells good!")



viper = Snake()

print(viper.cold_blooded) # returns True (taken from Reptile attributes)
print(viper.slither()) # Stick out my tongue...smells good!
