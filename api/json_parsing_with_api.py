import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# print(post_codes_req.status_code)  # 200
# print(post_codes_req.content)  # b'{"status":200,"result":{"postcode":"SE12 0NB", ...etc.
# print(type(post_codes_req.content))  # <class 'bytes'>
# print(post_codes_req.headers)  # {'Server': 'nginx/1.14.0', 'Date': ...etc.
# print(type(post_codes_req.headers))  # <class 'requests.structures.CaseInsensitiveDict'>
# print(post_codes_req)  # <Response [200]>

# print(post_codes_req.status_code)

# first iteration manually checking codes
# if post_codes_req.status_code == 200:
#     print(" success! ")
# elif post_codes_req.status_code == 404:
#     print(" sorry page unavailable ")

# second iteration using built in functionality (not explicitly defining the status codes)
# if post_codes_req.status_code:
#     print(" success! ")
# elif post_codes_req.status_code:
#     print(" sorry page unavailable ")

# third iteration using class and method
# class Status_Code:
#     # Getting user input of url
#     def __init__(self, url):
#         self.url = url
#
#     def check_status_code(self):
#         # Getting status of website, using requests function
#         self.post_codes_req = requests.get(self.url)
#         print(self.post_codes_req.status_code)
#
#
#
# class Live_Web_Status_Code(Status_Code):
#
#     def check_status_code(self):
#         post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
#         if post_codes_req.status_code:
#             return " success! "
#         elif post_codes_req.status_code:
#             return " sorry page unavailable "
#         return post_codes_req.content
#
# status = Live_Web_Status_Code()
#
# print(status.check_status_code())


json_data = post_codes_req.json()


for key in json_data:
    print(key)  # status and result

print(json_data)  # dictionary inside a dictionary

# from postcode api
# fetch data by key value pairs within dictionaries
# create a function to return the above values (key:value)
# create a class and move the code block inside the class


