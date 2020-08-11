
# create 4 individual classes that take a name and age
# each has a method (intro) to introduce themselves giving their identity, name and age
# each has a method (make_noise) to make their own respective noises

class Human:  # class Human - all the other classes will follow the same format and use the same methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):  # introduce self and give name and age
        print("I am a human being. My name is {}. I am {} years old".format(self.name, self.age))
        # one way of formatting a string using .format()

    def make_noise(self):  # make a noise!
        print("Doh!")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age}")
        # another way of formatting a string using f

    def make_noise(self):
        print("Woof!")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age}")

    def make_noise(self):
        print("Meow!")

class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am a bird. My name is {self.name}. I am {self.age}")

    def make_noise(self):
        print("Cheep!")

#  setting 4 objects for each class
human1 = Human("Homer", 45)
dog1 = Dog("Hector", 14)
cat1 = Cat("Jiji", 13)
birb1 = Bird("Petrie", 89)

#  iterate through the list to introduce each animal and their noise
for animal in (human1, dog1, cat1, birb1):
    animal.intro()
    animal.make_noise()
