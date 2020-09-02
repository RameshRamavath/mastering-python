'''
Class methods:

    By default regular methods automatically takes instance as the input **self

    How can we change it to take class as the input for a method - use decorator

    @classmethod - this makes a method as class method

'''

# change the raise amount at class level using classs method

class Employee:

    pay_raise = 1.04

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def apply_raise(self):
        return (self.pay * self.pay_raise)

    @classmethod
    def change_raise(cls, new_raise):
        cls.pay_raise = new_raise
        return cls.pay_raise

emp1 = Employee('Ramesh', 50000)
emp2 = Employee('Mahesh', 60000)

# all three will have same pay_raise value = 1.04  - let's say we want to change it to 1.05 at class level
print("Initial pay raise")
print(Employee.pay_raise)
print(emp1.pay_raise)
print(emp2.pay_raise)

# change pay raise

Employee.change_raise(1.05)

print("Pay raise post announcement")

print(Employee.pay_raise)
print(emp1.pay_raise)
print(emp2.pay_raise)

# class methods can be used as alternative constructors
# given input string - create instance of Employee from it


class Empclass:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

emp_string1 = 'Ramavath-Ramesh-50000'
emp_string2 = 'Ramavath-Ravi-60000'

new_emp1 = Empclass.from_string(emp_string1)
print(f"new employee details :: {new_emp1.first} {new_emp1.last} {new_emp1.pay}")

'''
Static methods - these methods doesn't take instance/class as arguments -
simply behaves like normal python functions - but since we have some logical connection with class we place them into our class
'''

class EmpStatic:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

import datetime
mydate = datetime.date(2020, 8, 20)
print(mydate)
print(EmpStatic.is_workday(mydate))