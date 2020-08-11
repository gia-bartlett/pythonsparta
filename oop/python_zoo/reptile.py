from animal import Animal
# importing the attributes from Animal class in animal file

class Reptile(Animal):  # name class (taking attributes from Animal as well)

    def __init__(self):  # define initial variables for all reptiles
        super().__init__() # inheriting initial variables from Animal
        self.cold_blooded = True # most reptiles are cold-blooded
        self.diurnal = True # reptiles have two eyes
        self.oviparous = True # reptiles lay eggs

    def warm(self):
        print("Find a sunny spot")

    def shed(self):
        print("Time to change my outfit")



gecko = Reptile()

print(gecko.alive) # returns True
print(gecko.warm()) # returns Find a sunny spot
print(gecko.fight())

# not sure why the dog call runs from animal on the page as well?

