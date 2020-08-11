from oop.more_oop_zoo import Animal

class Dog(Animal):

    species = "canine"

    def bark(self):
        return "woof"

class Cat(Animal):

    species = "feline"

    def meow(self):
        return "meow"

my_dog = Dog("Hector", "tan and white", 14, "canine")
print(my_dog.bark())

