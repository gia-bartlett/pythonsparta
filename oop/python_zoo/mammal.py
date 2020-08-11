from animal import Animal
# importing the attributes from Animal class in animal file

class Mammal(Animal):  # name class (taking attributes from Animal as well)

    def __init__(self, name, age, classification, weight, order):  # define initial variables for all mammals
        super().__init__(name, age, classification, weight) # inheriting initial variables from Animal
        self.order = order
        self.warm_blooded = True # all mammals are cold-blooded
        self.diurnal = True # mammals have two eyes

    def swim(self):
        print("I can swim - even if I don't like it!")

    def coat(self):
        print("I'm so fluffy!!")



my_dog = Mammal("Hector", 14, "mammal", 10)

print(my_dog)
my_dog.eat()
