# import json
# create a class Exchange_Rates
# add required attributes
# fetch data from exchange_rates.json
# display the data
# display the type of data
# display exchange rates with specific currencies

import json

class Exchange_Rates:
    def __init__(self):  # initialise the class
        with open("exchange_rates.json") as rates:  # open the file and give it an alias
            rate = json.load(rates)  # creating a variable and storing the data taken from rates above
            for r in rate:  # creating a for loop to iterate through the rate dictionary
                if r == "rates":
                    print(rate["rates"])  # print out all the rates for user to see
                    # print(rate)  # print the whole data to see what we have
                    # print(type(rate))  # print the type of data
            currency = input("Choose currency: ").upper()  #use input to choose currency from list printed above
            # added in .upper() so that user can input in lower case on computer will still understand
            print(rate["rates"][currency])  # prints chosen currency
            # print(rate["rates"]["GBP"])  # test to see how this statement works to choose certain currencies

r = Exchange_Rates()


