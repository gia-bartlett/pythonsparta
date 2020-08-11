# Homework 30/06
# 1. create a vairable called first_name and last_name
# create a variable called full_name and display full name

# first_name = input("Please print your first name ")
# last_name = input("Please print your last name ")
# age = input("Please print your age ")
# address = input("Please print your address ")
#
# full_name = first_name + " " + last_name + ", " + age + ", " + address
#
# print(full_name)
#
# # 2. create a string and loop through the string
# # print the string on one line
# # option 1
# city = "London"
# for letter in city:
#     print(letter, end = '')
# # option 2
# city = "London"
# one_line = ""
# for letter in city:
#     one_line += letter
# print(one_line)
#
# # 3. create a dictionary with employee records min 5 key:value pairs
# employee_record = {
#     "first_name": "Georgina",
#     "last_name": "Bartlett",
#     "employee": "Sparta",
#     "title": "trainee",
#     "city": "Coventry"
# }
#
# # print(employee_record)
# # using for loop iterate through
# for key, value in employee_record.items():
#     print(key, "=", value)
#
# # display the values and keys of the dictionary
#
# # 4. write a if..else statement to admit correct ages into the cinema
# # U, PG, 12a, 15, 18
#
# parent_present = "n" # setting to default value
#
# movie = str(input("What is the rating of the movie? U, PG, 12A, 15 or 18 ")).upper()
# age = int(input("How old are you? "))
#
#
# if movie == "12A" or movie == "PG":
#     parent_present = input("Will there be an adult present? y/n ").lower()
#
# # program just continues if it isn't a 12a
#
# if age >= 18 and movie == "18":
#     print("Enjoy your movie!")
# elif age >= 15 and movie == "15":
#     print("Enjoy your movie!")
# elif age >= 12 and movie == "12A":
#     print("Enjoy your movie!")
# elif age >= 0 and movie == "12A" and parent_present == "y":
#     print("Enjoy your movie!")
# elif age >= 8 and movie == "PG":
#     print("Enjoy your movie!")
# elif age >= 0 and movie == "PG" and parent_present == "y":
#     print("Enjoy your movie!")
# elif age > 0 and movie == "U":
#     print("Enjoy your movie!")
# else:
#     print("Sorry, you're not old enough or need an adult present!")
#
#
# convert a number into cm or inches
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
#
## continue dog class from today
## add more attributes sleep, breathe, run, eat, fetch
#
# class Dog:
#
#     animal_kind = "canine"
#
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#
#     def bark(self):
#         return "woof"
#
#     def sleep(self):
#         return "dreaming"
#
#     def breathe(self):
#         return "panting"
#
#     def eat(self):
#         return "nomming"
#
#     def fetch(self):
#         return "chasing"
#
#
# my_dog = Dog("Hector", "tan and white")
# print(my_dog.bark())
# print(my_dog.animal_kind)
