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

age = 6
movie = "PG"
parent_present = True

if age >= 18 and movie == 18:
    print("Enjoy your movie!")
elif age >= 15 and movie == 15:
    print("Enjoy your movie!")
elif age >= 12 and movie == "12a":
    print("Enjoy your movie!")
elif age >= 0 and movie == "12a" and parent_present == True:
    print("Enjoy your movie!")
elif age >= 8 and movie == "PG":
    print("Enjoy your movie!")
elif age >= 0 and movie == "PG" and parent_present == True:
    print("Enjoy your movie!")
elif age > 0 and movie == "U":
    print("Enjoy your movie!")
else:
    print("Sorry, you're not old enough!")
