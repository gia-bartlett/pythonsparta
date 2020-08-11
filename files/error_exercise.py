# Accept from the user some text.Ensure user enters something else raise an
# exception.
# After that# write#that# text# to# a file and then read
# from this file to write# to another file simultaneously
import math


def split_cheque(total, number_of_people):  # function to split the check after a meal
    return math.ceil(total / number_of_people)  # will return the rounded up figure of total divided by number of people


def bill_splitter():
    total_due = 0
    while total_due == 0:
        try:
            total_due = float(input("What is the total? "))
        except ValueError as err:
            print("Error: Please enter the total as a whole number or decimal")
    # likely to be a float as it is the cheque
    number_of_people = 0
    while number_of_people <= 0:
        try:
            number_of_people = int(input("How many people? "))
            if number_of_people <= 1:
                raise ValueError("More than one person is required for the cheque to be split!")
            #  Added this raise value error to prevent the cheque being divided by 0 or a minus number
        except ValueError as err:  # this is the error that will eb thrown if someone enters the wrong value (str)
            print("Error: Please enter a number! ")
            print(f"{err}")
    # likely to be an int but may be entered as a string and throw an error
    amount_due = split_cheque(total_due, number_of_people)
    print(f"Each person owes £{amount_due}")

# ValueError - entering a str where an int or float was expected
# NameError - total_due does not get assigned if an error is thrown
# so we need to add the else statement so the code continues
# ZeroDivisionError - saying there are 0 people

bill_splitter()