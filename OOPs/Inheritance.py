'''

Using functionality of main class in dependent/child classes - by extending/ completely modifying them

'''


# *** create developers and managers from Employee class {names, emails and pay will be common for all of them}

class Employee:
    pay_rasie = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def apply_raise(self):
        return int(self.pay * self.pay_rasie)


emp1 = Employee('Ramavath', 'Ramesh', 50000)
print("Employee email : ", emp1.email)  # Employee email :  Ramavath.Ramesh@company.com


# create developer class and inherit from employee class


# class Developer(Employee):  # using class behaviour without modifying it {it will have all variables and methods
# from Employee}
#
#   pass
#
# dev1 = Developer('Ramavath', 'Ramesh', 50000) # Developer email :  Ramavath.Ramesh@company.com
# print("Developer email : ", dev1.email)
# print(help(Developer)  - this will give method resolution order

# *** add feature to change the raise_pay and add prog_lang to developer

class Developer(Employee):
    pay_rasie = 1.05  # changed only at sub-class level without touching main class variables

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # no need to give self.variable for parent class variables
        self.prog_lang = prog_lang


print("Employee level raise", Employee.apply_raise(emp1))
developer1 = Developer('Mahesh', 'Naik', 50000, 'Java')
print("Developer level raise", Developer.apply_raise(developer1))

developer2 = Developer('Ravi', 'Naik', 60000, 'Python')
# get email from parent class and prog lang from sub-class
print(
    f'Developer 2 Email {developer2.email} and Programming Language {developer2.prog_lang}')  # Developer 2 Email Ravi.Naik@company.com and Programming Language Python


# ** write a manager class which handles employees under manager

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # method to add an employee under the manager

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(f'--> {emp.first} {emp.last}')


manager1 = Manager('Sumit', 'Kumar', 80000, [developer1])
print('Manager email id :', manager1.email)
manager1.print_employees()
manager1.add_emp(developer2)
manager1.print_employees()

manager1.remove_emp(developer1)
manager1.print_employees()

# how to check if a class is inherited from another - isinstance/ issubclass methods

print(isinstance(manager1, Manager))
print(isinstance(manager1, Developer))  # False - because manager1 is not inherited from Developer
print(isinstance(manager1, Employee))  # True - because manager1 is inherited from Employee

print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Developer))  # False
