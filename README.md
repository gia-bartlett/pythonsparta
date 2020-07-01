#Python Notes:
efficient
scalable
open-source (well-resourced)

all python is in lower case
no spaces - separate text with underscore
indexing starts from 0 in python (1 in SQL)

(#) to comment in Python
select all CTRL / to comment multiple lines out

x and y are not good naming conventions. Nor can you use reserved characters (string, int etc).
Be more descriptive with names of variables.
Include comments - future you with appreciate it!

"double quotes" v 'single quotes'
No real difference but double is better because of apostrophes in text:
"O'Brien"
'O\'Brien'
'\"Hey Bob!\"'
Use backslash \ to cancel out any quotes within strings

###VARIABLES:
x = 10 (integer)
y = 3.5 (float)
name = "James" (string)

###PRINT:
The print() function prints the specified message to the screen, or other standard output device.
The message can be a string, or any other object, the object will be converted into a string before written to the screen.
print(x) (will print 10)

###INPUT:
The input() method reads a line from input, converts into a string and returns it.
The syntax of input() method is: input("prompt ") OR input([prompt])
Leave a space after prompt otherwise the answer will be squashed against the prompt.

###INDEXING:
H E L L O   W O R L D  !
0 1 2 3 4 5 6 7 8 9 10 11
print("Hello World!"[1:5]); #ello
Starts at 0 and prints up to one before the last number


###METHODS:
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

###LISTS:
Java - array
Python - list
To store data in a variable. Better than a string because you can add and take away.
Better for managing data. Lists are ordered.
Easier to add, remove etc.

[Syntax]
list[] =:
lists are mutable - can be changed
tuple() =:
lists are immutable - they can't be edited once they've been created
* if an error is made with a tuple it must be converted to a list and corrected
dictionary{} - key:value:
stores the data with key:value pairs
age:14
name:"Hector"
breed:dog