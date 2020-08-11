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

