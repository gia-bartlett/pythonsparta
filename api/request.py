import requests
import status_codes

# check HTTP/HTTPS
# 200 - success
# 400 (404 - page not found)

# create a variable

response_bbc = requests.get("https://www.bbc.co.uk/")

print(response_bbc.status_code)  # retrieves the status code to base ifs
print(response_bbc.headers)  # retrieves the HTML header
print(type(response_bbc.headers))  # type of header
print(response_bbc.content)  # prints a jumble of HTML content (what you're looking for)

# 1st iteration
# receive a response and check
if response_bbc.status_code == 200:
    print("Success!")
elif response_bbc.status_code == 404:
    print("Page not found")
else:
    print("Sorry something went wrong")

# 2nd iteration
# take the above an put it in a function --> saved in status_codes


# 3rd iteration oop with 4 pillars
# importing status_codes file which contains the function to check the status codes

class Status:
    status_codes.check_response_code()

Status()