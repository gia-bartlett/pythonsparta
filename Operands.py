from random import random
import math
# # OPERANDS:
# # + | - | * | / | % (addition, subtraction, multplication, division, remainder)
# # > | < (greater than, less than)
# # == | != (equal to, not equal to)
# # >= | <= (greater than or equal to, less than or equal to)
#
# # x = 10
# # y = 12
# #
# # print(x == y) #False
# # print(x<=y) #True
# # print(x * y) #120
# # print(y % x) #2 (12 into 10 leaves 2 remaining)
#
# # float_num = 24.5
# #
# # # round  a float
# # print(math.ceil(float_num)) # round up
# # print(math.floor(float_num)) # round down
# # # print(random()) # just prints a random number
#
# calculate a method that takes two arguments to calculate cm and inches
# 1 cm / 2.54 = 1 inch
# 1 inch * 2.54 = 1 cm

# # convert to inches
# def conversion_inches(num):
#
#     return(math.ceil(num / 2.54))
#
# print(conversion_inches(6))
#
# # convert to cm
# def conversion_cm(num):
#
#     return(math.ceil(num * 2.54))
#
# print(conversion_cm(6))
#
# convert both
def conversion():
    qualification = str(input("Are you converting to inches or cm? in/cm "))
    measurement = int(input("Please enter your measurement: "))
    if qualification == "in":
        return measurement / 2.54
    elif qualification == "cm":
        return measurement * 2.54
    else:
        print("Please try again")

print(conversion())
