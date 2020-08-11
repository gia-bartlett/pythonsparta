from student_data import Student

class DevOps(Student):  # subclass for devs

    def __init__(self, first, last, prog_lang):
        super().__init__(first, last) # copies the init code from above and allows it to handle the input
        self.prog_lang = prog_lang

dev1 = DevOps("Georgina", "Bartlett", "Python")  # will try to init via Developer but as
# there is no init it will move up the chain til it finds what it is looking for


print(dev1.prog_lang)
print(dev1.full_name())