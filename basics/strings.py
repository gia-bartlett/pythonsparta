# strings - indexing - casting - slicing - concatentation

greeting_welcome = "Hello World!"
#welcome_user = input("Please enter your name ")

#H E L L O   W O R L D  !
#0 1 2 3 4 5 6 7 8 9 10 11

print(len(greeting_welcome)); #12

#print("Dear " + welcome_user + ", welcome on board!");

#Slicing strings
print(greeting_welcome[0]); #H
print(greeting_welcome[10]); #d
print(greeting_welcome[1:5]); #ello
print(greeting_welcome[6:11]); #World
print(greeting_welcome[0:3]); #Hel

#reverse indexing
print(greeting_welcome[-5]); #o
print(greeting_welcome[-6]); #W
print(greeting_welcome[-6:-1]); #World

remove_white_space = "Remove white space at the end of a string           "
print(len(remove_white_space)); #52

print(len(remove_white_space.strip())) #41

print(remove_white_space.strip()) #strips the white space off the end