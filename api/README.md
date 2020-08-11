### APIs

* Application programming interface
* used to connect to other programs
* module called requests to interact with web-apis
* pip install requests in the terminal  

HTTP Status Codes:  
1. Informational responses (100–199)  
2. Successful responses (200–299)  
3. Redirects (300–399) 
4. Client errors (400–499)  
5. Server errors (500–599)  

https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

API calls to web browser


CRUD  
- create
- read
- update
- delete  
These are the four basic database operations.  
Many HTTP services also model CRUD operations through REST APIs

### JSON  
https://www.w3schools.com/whatis/whatis_json.asp  
https://www.w3schools.com/js/js_json_intro.asp  

What is JSON?  
Javascript Object Notation  

<img src = "https://shareurcodes.com/photos//rest-api.jpg">  

json is syntax for exchanging data between a browser and a server  

- JSON is text, and we can convert any JavaScript object into JSON, and send JSON to the server.  
- We can also convert any JSON received from the server into JavaScript objects   
```
Data types:
a sting ("Hello World!")
a number ("3") --> within quotes
an object (json object)
a boolean (True/False)
NULL
```
This way we can work with the data as JavaScript objects, with no complicated parsing and translations.  

Data is in name/value pairs (like a dictionary) and separated by commas:  
```
{"name": "James", "age": "30"}
```
JSON names require double quotes. JavaScript names do not.  

JSON objects are written inside curly braces:
```
{"firstName":"John", "lastName":"Doe"}
```

```python
import json

# ENCODING from dictionary and writing jsonfile
car_data = {"name": "tesla", "engine": "electric"}  # dictionary
print(car_data)  # print the dictionary
print(type(car_data))  # check the type of dictionary

car_data_json_string = json.dumps(car_data)
# json.dumps changes python dict to json str
print(type(car_data_json_string))  # json format changed the type to a str

# Let's create a jsonfile with writing permission

with open("new_json_file.json", "w") as jsonfile:  # .json is file type, "w" is permission type (write)
# as is an alias just like in SQL (we don't want to keep rewriting a long filename)

    json.dump(car_data, jsonfile)  # json.dump takes two arguments:
# dictionary, file_type

with open("new_json_file.json") as jsonfile:  # Decoding
    # Reading from the file we have just created
    car = json.load(jsonfile)  # storing data from file to car variable
    print(type(car))  # checking type of data again
    print(car["name"])  # to get the value stored in key called "name"
    print(car["engine"])  # to get the value stored in key called "engine"

# We have DECODED our file mew_json that we created above
# We used dumps(), dump() and load() methods
```

Encode - write  
Decode - read  

Full path of file location needed if saved elsewhere
