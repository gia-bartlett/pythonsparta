
from student_data import Student


# Creating a child class of Coding
class Coding(Student):
    # Intialising the class. int converts the inputs to the correct data type.
    def __init__(self, code_lines):
        self.code_lines = int(code_lines)

    def write_code(self):
        coding = int(input("How many lines of code would you like to write? "))
        self.code_lines = self.code_lines + coding

    def commit(self):
        print("You've written {} lines of code!".format(self.code_lines))

code1 = Coding(1)
Coding.write_code(code1)
Coding.commit(code1)
