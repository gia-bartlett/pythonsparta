#DATA TYPES:

#Boolean Values:

use_text = "here's SOME text with lots of text"

print(use_text.count("t")); #6
print(use_text.count("S")); #1 (case sensitive)

print(use_text.lower()); #prints the variable in lower case
print(use_text.upper()); #prints the variable in UPPER CASE
print(use_text.capitalize()); #Capitalize the first letter of the string (everything else into lowercase)

print(use_text.replace("text","love")); #replaces any instance of one thing with chosen other thing [old text, new text]

print(use_text.startswith("h")); #returns True in this instance - useful for if statements