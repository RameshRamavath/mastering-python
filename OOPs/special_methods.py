# **** Change the way we print class object and object as string


"""

Dunder methods -- methods which starts with double underscore (__) on both sides

"""


class Employee:
    def __init__(self, fullname, email):
        self.fullname = fullname
        self.email = email

    def __str__(self):
        return "{} - {}".format(self.fullname, self.email)

    def __repr__(self):
        return "Employee ('{}', '{}')".format(self.fullname, self.email)

    def __len__(self):  # dunder len for Employee class will give me len of emp full name
        return len(self.fullname)


emp1 = Employee('Ramesh Naik', 'naik@gmail.com')

print(repr(emp1))
print(str(emp1))

print(emp1.__repr__())
print(emp1.__str__())  # exactly same as above two lines

print(len('Ramesh Naik'))
print(len(emp1))
