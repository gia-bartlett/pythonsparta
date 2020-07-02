#Python Notes:
* efficient
* scalable
* open-source (well-resourced)

###Format:
* all python is in lower case
* no spaces - separate text with underscore
* indexing starts from 0 in python (1 in SQL)
* (#) to comment in Python (single line)

###Tips for PyCharm
* select all CTRL / to comment multiple lines out
* CTRL SHIFT up down - move whole line up or down
* CTRL SHIFT left right - select whole words
* CTRL up down - move page up and down
* CTRL left right - skip whole words with cursor
* SHIFT up down - select whole lines

x and y are not good naming conventions. Nor can you use reserved characters (string, int etc).
Be more descriptive with names of variables.
Include comments - future you with appreciate it!

"double quotes" v 'single quotes'
No real difference but double is better because of apostrophes in text:
"O'Brien"
'O\'Brien'
'\"Hey Bob!\"'
Use backslash \ to cancel out any quotes within strings

####VARIABLES:
x = 10 (integer)
y = 3.5 (float)
name = "James" (string)

* placeholder 

####PRINT:
The print() function prints the specified message to the screen, or other standard output device.
The message can be a string, or any other object, the object will be converted into a string before written to the screen.
print(x) (will print 10)

####INPUT:
* The input() method reads a line from input, converts into a string and returns it.
* Allows a user to input the variable
* The syntax of input() method is: input("prompt ") OR input([prompt])
* Leave a space after prompt otherwise the answer will be squashed against the prompt.

####INDEXING:
H E L L O   W O R L D  !
0 1 2 3 4 5 6 7 8 9 10 11
print("Hello World!"[1:5]); #ello
Starts at 0 and prints up to one before the last number


####METHODS:
cast()
The cast() function convert a variable value from one type to another.
This is, in Python, done with functions such as int() or float() or str()

len()
The len() function returns the number of items in an object.
When the object is a string, the len() function returns the number of characters in the string.

.count()
The .count() method returns the number of occurrences of substring sub in the range [start, end].
Optional arguments start and end are interpreted as in slice notation.

.lower()
.upper()
returns a copy of the string in which all case-based characters have either been lowercased
or UPPERCASED
Plenty of others to explore following the .

concatenation:
String concatenation means add strings together.
Use the + character to add a variable to another variable
To add a space between them, add a " "
remember - + with numbers means add!

####LISTS:
ordered
Java - array
Python - list
To store data in a variable. Better than a string because you can add and take away.
Better for managing data. Lists are ordered.
Easier to add, remove etc.

[Syntax]
list[] =:
lists are mutable - can be changed
14, "Hector", "dog"

tuple() =:
lists are immutable - they can't be edited once they've been created
* if an error is made with a tuple it must be converted to a list and corrected
14, "Hector", "dog"

dictionary = {"":""} - key:value:
stores the data with key:value pairs
more dynamic than lists and tuples
age:14
name:"Hector"
breed:dog

sets:
unordered (unlike list which are ordered)
uses {}


##CONTROL FLOW
and/or:
same as SQL (AND - both must be true. OR - either condition needs to be true)

if:
if this condition is met - do this

elif:
used as if, after first if

else:
otherwise do this

####for loops:
* iterate through a list, string, dictionary or tuple
* collects large amount of information quickly
for <variable> in <whatever you want to iterate through>:
    print(<variable>)
    
####while loops:
* runs until a condition is true


##FUNCTIONS:

* Why do we use functions? What are the benefits?
* Reuse code - DRY (Don't Repeat Yourself)
* Python has functions built in that we can use (print(), format(), len(), etc.)
* Functions should only do one job
* We can also create our own to reuse blocks of code we have written:
* SYNTAX:
def <name of function>(parameter1, parameter2,.....):
    <function instructions>
* A function must be called
*

