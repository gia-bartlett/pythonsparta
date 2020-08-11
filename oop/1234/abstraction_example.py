from payment_types import epay
from payment_types import credit
from payment_types import debit

# importing abstracted functions from payment_types

class Payment:  # main parent class that will deal with the payment
    amount = float(input("Please enter your total: "))  # user input for total
    payment_choice = int(input("How would you like to pay? 1. ePay 2. Credit Card 3. Debit Card "))  #user input for payment type

    if payment_choice == 1:
        print("Your total is £{:.2f}".format(epay(amount)))  # calls the epay function
    elif payment_choice == 2:
        print("Credit Card incurs a 5% surcharge. Your total is £{:.2f}".format(credit(amount)))  # calls the credit function
    elif payment_choice == 3:
        print("Debit Card incurs a £1 fee. Your total is £{:.2f}".format(debit(amount)))  # calls the debit function
    else:
        print("Sorry, we no longer accept cash payments")
    # {:.2f} gives the total to 2 decimal places






