import requests


def check_response_code():
    response_bbc = requests.get("https://www.bbc.co.uk/")

    if response_bbc.status_code == 200:
        print("Success!")
    elif response_bbc.status_code == 404:
        print("Page not found!")
    else:
        print("Sorry, something went wrong!")
    return response_bbc.content

