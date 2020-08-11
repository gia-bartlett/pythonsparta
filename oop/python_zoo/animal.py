

class Animal:  # name class

    def __init__(self, name, age, classification, weight):  # define initial variables for all animals
        self.name = name
        self.age = age
        self.classification = classification
        self.weight = weight
        self.alive = True
        self.hunger = 0
        self.happiness = 10

# introduce animals
    def __str__(self):
        return "Meet {}, they are {} years old. They are a {}. They weigh {}kgs!".format(self.name, self.age, self.classification, self.weight)

    def eat(self):
        food = int(input("How many portions do you want to feed {}? ".format(self.name)))
        self.hunger -= food
        if self.hunger < 0:
            print("{} they are going to get fat!".format(self.name))
        print("nom nom nom")

    def pet(self):
        pets = input("How many times to you want to pet {}? ".format(self.name))
        self.happiness += pets
        if self.happiness == 10
            print("That's enough pets for now!")
        print("They really enjoy being stroked!")

    def breathe(self):
        print("ah... Fresh air")

    def fight(self):
        print("Come at me bro!")

    def flee(self):
        print("RUN AWAY!!!")


