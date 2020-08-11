class Student:


    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@company.com"
        self.__minsalary = 10



    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def salary(self):
        print("Salary: {}".format(self.__minsalary))

    def __repr__(self):  # unambiguous representation of the object
        return "Employee('{}', '{}': {})".format(self.first, self.last, self.email) # creating something that can be pasted back into Python
        # a string the we can use to recreate the object
    # if you don't have a repr then Python will default to repr
    def __str__(self):  # readable representation of the object
        return '{} - {}'. format(self.full_name(), self.email)
