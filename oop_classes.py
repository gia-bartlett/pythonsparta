# create a class method with key word class

# class Python_Calculator:
#
#     def add_values(self, num1, num2): # self keyword refors to the class
#         pass # for testing, remember?
#
# # create a basic calculator inside a class
# # should have methods to add, subtract, divide, modulo
# # create an object of a class
# # run the class

# ask the user to choose what they'd like ot do

class Python_Calculator:

    def __init__(self, num1, num2): # initialise the class (create a variable inside the class)
        self.num1 = num1
        self.num2 = num2

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "You can't divide by zero"
        else:
            return num1 / num2

    def remainder(self, num1, num2):
        return num1 % num2

# user input to get the numbers they're using
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# refer to the class
maths = Python_Calculator() # object
# set the input
choice = 1 # operation

while choice != 0:
    # get from the user what they want to do
    print("Choose 1 for addition")
    print("Choose 2 for subtraction")
    print("Choose 3 for multiplication")
    print("Choose 4 for division")
    print("Choose 5 for remainder")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        print(maths.addition(num1, num2))
        break
    elif choice == 2:
        print(maths.subtraction(num1, num2))
        break
    elif choice == 3:
        print(maths.multiplication(num1, num2))
        break
    elif choice == 4:
        print(maths.division(num1, num2))
        break
    elif choice == 5:
        print(maths.remainder(num1, num2))
        break
    else:
        print("Please choose: 1, 2, 3, 4 or 5!")



