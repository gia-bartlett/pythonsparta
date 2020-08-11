from student_data import Student

class DevOps(Student):  # subclass for devs

    def __init__(self, first, last, prog_lang):
        super().__init__(first, last) # copies the init code from above and allows it to handle the input
        self.prog_lang = prog_lang

    def __len__(self):  # len(emp1) to call
        return len(self.full_name())

dev1 = DevOps("Georgina", "Bartlett", "Python")  # will try to init via Developer but as
# there is no init it will move up the chain til it finds what it is looking for


dev1.__minsalary = 1000
dev1.salary() # this doesn't work because it is a private method