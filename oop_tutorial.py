
class Employee:
    # pass # allows you to leave the function empty until you need to use it
    raise_amount = 2 # declare a class variable up here

    def __init__(self, first, last, position, pay):
        self.first = first
        self.last = last
        self.position = position
        self.pay = float(pay)
        self.email = first + '.' + last + "@company.com"

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def annual_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # by referencing the class variable (raise_amount) this will ALWAYS reference that even if the instace has been changed
        #self.pay = int(self.pay * self.raise_amount)
        # If this isn't otherwise set it will default to the class but can be set individually


emp1 = Employee("Georgina", "Bartlett", "Kohai", 20)
emp2 = Employee("James", "Knight", "Sensei", 1000001)

# each instance of Employee will take a different piece of memory

# writing out each employee would take a long time

print(emp1.email)
print(emp2.email)

# print("{} {}".format(emp1.first, emp1.last))
# this is a lot of code to write each time you want to print your employees' full name
# what if you have 10,000 employees?
# so we'll create a method

print(emp2.full_name()) # calling the method doesn't need an argument when using an instance
print(Employee.full_name(emp1)) # calling the method on the class it needs the instance entering

print(emp1.raise_amount) # 2
print(emp1.pay) # current pay
emp1.annual_raise() # apply raise class variable
print(emp1.pay) # new pay

print(emp1.__dict__) # namespace
# {'first': 'Georgina', 'last': 'Bartlett', 'position': 'Kohai', 'pay': 40, 'email': 'Georgina.Bartlett@company.com'}

#lets give George a massive payrise!

emp1.raise_amount = 10000

print(emp1.raise_amount)
print(emp2.raise_amount)

emp1.annual_raise()

print(emp1.pay)