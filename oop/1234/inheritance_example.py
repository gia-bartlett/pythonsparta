# creating a parent class called Employee
# Employees all have a first name, last name, base pay, email

class Employee:

    def __init__(self, first, last, base_pay):
        self.first = first
        self.last = last
        self.base_pay = float(base_pay)
        self.email = first + "." + last + "@company.com"  # creates the email from the first and last name input

    def full_name(self):
        return "{} {}".format(self.first, self.last)

class Coders(Employee):  # subclass Coders will inherit from the parent Employee

    # created a dictionary to handle the bonus amount based on skills
    bonus_structure = {
        "Python" : 1.04,
        "SQL" : 1.03,
        "Java" : 1.05
    }

    def __init__(self, first, last, base_pay, prog_lang):  # adding programming language to the init (unique to Deparment)
        super().__init__(first, last, base_pay)  # copies the init from Employee and allows it to handle the input from there
        self.prog_lang = prog_lang
        self.full_pay = float(self.base_pay * Coders.bonus_structure[self.prog_lang])
        # taking the base pay and multiplying it by the equivalent in the dictionary
        # calculate full pay using the the set_full_pay method below

    def __repr__(self):  # unambiguous representation of the object
        return "Employee('{}', '{}', {}, '{}')".format(self.first, self.last, self.base_pay, self.prog_lang) # creating something that can be pasted back into Python
        # a string the we can use to recreate the object
    #  if you don't have a str then Python will default to repr
    def __str__(self):  # readable representation of the object
        return 'Name: {} - {} Pay: £{:.2f}'. format(self.full_name(), self.email, self.full_pay)


dep1 = Coders("Georgina", "Bartlett", 5, "Python")
dep2 = Coders("James", "Knight", 6, "SQL")
dep3 = Coders("Hector", "Bartlett", 10, "Java")

print(dep1) # prints: Name: Georgina Bartlett - Georgina.Bartlett@company.com Pay: £5.20

