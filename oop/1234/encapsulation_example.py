
class Apples:  # creating a class to buy and sell apples

    def __init__(self, variety):
        self.variety = variety
        self.__max_purchase = 2  # setting the maximum purchase price
        self.__min_sale = 3  # setting the minimum sale price

    def buy(self):  # method to buy apples
        print(f"The maximum we can pay for each apple is {self.__max_purchase}p")

    def sell(self):  # method to sell apples
        print(f"These apples are for sale for {self.__min_sale}p each and not a bean less!")

    def set_max(self, price):  # setter to allow the alteration of the max purchase price
        self.__max_purchase = price

    def set_min(self, price):  # setter to allow the alteration of the min sale price
        self.__min_sale = price

a = Apples("Gala")
a.sell()  # "These apples are for sale for 3p each and not a bean less!"

# change the minimum sale price from 3 to 2
a.__min_sale = 2
a.sell()  # "These apples are for sale for 3p each and not a bean less!"

# change the minimum sale price from 3 to 2 using the setter function
a.set_min(2)  # using the set_min method
a.sell()  # "These apples are for sale for 2p each and not a bean less!"

