import requests
import json

# 1st iteration:
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb").content  # python object has a load of attributes when it arrives
# # one of which is content. This generally contains what you want. SO by using .content then you are accessing just content.
# # that gives you an object in JSON format and you need to unpack it (.loads)
# data = json.loads(post_codes_req)
# # now the variable data is a dictionary which contains all the information you can access accordingly
# print(data)  # test
# print(data["result"]["region"])

# 2nd iteration:
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb").content
# data = json.loads(post_codes_req)
#
# def dictionary_iterator(nested_dict):
#     for key, value in nested_dict.items():
#         print(type(value))
#         if type(value) is dict:
#             dictionary_iterator(value)
#         else:
#             print(key, " : ", value)
#
# dictionary_iterator(data)

# 3rd iteration:
class Json_Dict:  # created a class

    def __init__(self, url):  # initialise the class to accept a url (reusability)
        self.url = url
        self.data = json.loads(requests.get(url).content)  # turn the url get into dict

    def dictionary_iterator(self, data):
        for key, value in data.items():
#           if type(value) is dict:
#               self.dictionary_iterator(value)  --> this would NOT work and I could NOT work out why
            if str(type(value)) == "<class 'dict'>":
                print("dict detect")
                self.dictionary_iterator(value)
            else:
                print(key, " : ", value)

dict = Json_Dict("https://api.postcodes.io/postcodes/pl46pr")

dict.dictionary_iterator(dict.data)




