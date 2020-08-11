class Student:
    # num_of_emp = 0 # class variable (each time we create a new employee this will increase by 1)
    # raise_amount = 2 # declare a class variable up here

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@company.com"
        # Employee.num_of_emp += 1  # set in the init because the init runs each instance
        # # Employee is used instead of self because we are never going ot want/need to override this


    def full_name(self):
        return "{} {}".format(self.first, self.last)




