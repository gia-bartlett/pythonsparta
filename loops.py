#LOOPS:

# FOR loop:

list_data = [1, 2, 3, 4]
# print(list_data) # [1, 2, 3, 4]

# for data in list_data:
#     print(data); # prints 1 2 3 4 in a single line

# for data in list_data:
#     if data > 3:
#         break
#     print(data) # will print 1 2 3 but not 4 because we told the loop to break when it found anything greater than 3

# for data in list_data:
#     if data > 3:
#         print("YAS!")
#     elif data < 1:
#         print("please enter a number above 0")
#     print(data) # will print 1 2 3 YAS! 4
#
# create a string and loop through the string
# print the string on one line
## option 1
# city = "London"
# for letter in city:
#     print(letter, end = '')
## option 2



city = "London"
one_line = ""
for letter in city:
    one_line += letter
print(one_line)


# # WHILE loop:
# x = 1
#
# while x < 5:
#     print("it's working -> {x}")
#
#     x += 1 # without this it'll just keep iterating through forever!!!

