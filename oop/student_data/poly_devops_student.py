from student_data import Student

class DevOps(Student):  # subclass for devs

    def __init__(self, first, last, prog_lang):
        super().__init__(first, last) # copies the init code from above and allows it to handle the input
        self.prog_lang = prog_lang

    def intro(self):  # introduce self and give name and age
        print("I am a DevOps Engineer. My name is {}. I code in {}.".format(self.first, self.prog_lang))
        # one way of formatting a string using .format()


class Java(Student):  # subclass for devs

    def __init__(self, first, last, prog_lang):
        super().__init__(first, last)  # copies the init code from above and allows it to handle the input
        self.prog_lang = prog_lang

    def intro(self):  # introduce self and give name and age
        print("I am a Java Engineer. My name is {}. I code in {}.".format(self.first, self.prog_lang))
        # one way of formatting a string using .format()

dev1 = DevOps("Georgina", "Bartlett", "Python")
java1 = Java("Rick", "Roll", "Java")

for coder in (dev1, java1):
    coder.intro()