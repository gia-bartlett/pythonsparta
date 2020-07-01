# CONTROL FLOW:

# weather = "sunny"
#
# if weather == "sunny":
#     print("Let's go to the beach!")
# elif weather == "snowy":
#     print("Let's go skiing!")
# else:
#     print("Let's stay inside!")
#
# age = 18
#
# if age == 18 or age > 18 # if age >= 18
#     print("Please enjoy the movie!")
# else:
#     print("Sorry, you're not old enough!")

# write a if..else statement to admit correct ages into the cinema
# U, PG, 12a, 15, 18

parent_present = "n" #setting to default value

movie = str(input("What is the rating of the movie? U, PG, 12A, 15 or 18 ")).upper()
age = int(input("How old are you? "))


if movie == "12A" or movie == "PG":
    parent_present = input("Will there be an adult present? y/n ").lower()

# program just continues if it isn't a 12a

if age >= 18 and movie == "18":
    print("Enjoy your movie!")
elif age >= 15 and movie == "15":
    print("Enjoy your movie!")
elif age >= 12 and movie == "12A":
    print("Enjoy your movie!")
elif age >= 0 and movie == "12A" and parent_present == "y":
    print("Enjoy your movie!")
elif age >= 8 and movie == "PG":
    print("Enjoy your movie!")
elif age >= 0 and movie == "PG" and parent_present == "y":
    print("Enjoy your movie!")
elif age > 0 and movie == "U":
    print("Enjoy your movie!")
else:
    print("Sorry, you're not old enough or need an adult present!")


# break will break the loop