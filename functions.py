# FUNCTIONS

# def <name of function>(parameter1, parameter2,.....):
#     <instructions/code to run - called 'method'>

# example
def greeting():
    return "Hello World!" # return statement simply returns what follows it
    # pass - skip the function

print(greeting())

# example
def test():
    pass # will pass the method and there will be no outcome - used in creating or building a unit test

# make your own mini function
def sibling(sibling): # function call sibling takes one argument
    return(sibling + " is my brother")

print(sibling("Andrew")) # Andrew is my brother

# methods with parameters/arguments

def add_values():
    return 4 + 4 # we can return anything inc string + int

print(add_values()) # = 8
# this code can't be reused for anything other than 4 + 4

# this can be reused many times - all you need to do is change the arguments
def multiply_value(num1, num2): # if the function has parameters it will be expecting these as arguments when it is called
    return num1 * num2

print(multiply_value(2, 5)) # 10
print(multiply_value(3, 3)) # 9
print(multiply_value(5, 5)) # 25

# create a function with two parameters to return a subtraction of the values given:
def sub_value(num1, num2):
    return num1 - num2

print(sub_value(5, 5))
print(sub_value(2020, 1989))

# create a function with two parameters to return a division of the values given:
def div_value(num1, num2):
    return num1 / num2

print(div_value(12, 6))
print(div_value(100, 2))

# create a function with two parameters to return a modulo of the values given:
def mod_value(num1, num2):
    return num1 % num2

print(mod_value(11, 5))
print(mod_value(22, 7))

# Create a function with multiple args:

def multi_args(*multiargs): # use the * when you don't know the specific number of arguments
    # print(type(multiargs()))

    for args in multiargs:
        print(args)
    return args
print(multi_args(1, 2, 3, 4, 5))

# Have a user input into the function
def sub_value(num1, num2):
    return num1 - num2

num1 = int(input("Please choose a number. "))
num2 = int(input("Please choose a second number. "))

print(sub_value(num1, num2))

# OR

def sub_value2():
    num1 = int(input("Please choose a number. "))
    num2 = int(input("Please choose a second number. "))
    return num1 - num2

print(sub_value2())