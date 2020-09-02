# how to create class, how to create object from it
# how to assign values to member variables of Class

# ***** without init method or constructor  *****

class Student:
    pass


# student1 = Student('Ram') # TypeError: Student() takes no arguments
student1 = Student()
student2 = Student()

print(student1)
print(student2)

# note two diff objects/ memory location

student1.name = 'Ramesh'
student1.age = 30

student2.name = 'Mahesh'
student2.phone = 8189099494

print(student1.age)
print(student2.phone)


# ***** use __init__ method to declare instance variables/ attributes/ arguments/ variables *****

class Employee:
    # Class objects support two kinds of operations: attribute references and instantiation
    # name and age - attributes / Instance variables
    # instantiation - __init__ [similar to constructor in Java]

    # class variables  - same for all instances / shared by all instances
    company = "Western Union"

    def __init__(self, first, last, pay):  # name and age are instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    # write a functionality to display full name of employee - instead of manually doing every time - write a method
    # for it

    def display_fullname(self):
        return f"{self.first} {self.last}"


emp1 = Employee('Ramesh', 'Naik', 50000)
emp2 = Employee('Mohan', 'Naik', 60000)

# Every class will have default constructor / instantiation method - then assign values to member attributes
# emp3 = Employee
# emp3.name = "mahesh"
# emp3.age = 30

print(emp1.email + " default company :: " + emp1.company)
print(emp2.email + " default company :: " + emp2.company)

# call our method from class

print("Emp1 full name :: " + emp1.display_fullname())
print("Emp2 full name :: " + emp2.display_fullname())

# call method using class name

print("Using class :: " + Employee.display_fullname(emp1))

# *********** Class variables *********

'''
Class variables are variables which are shared among all the instances of class

'''


# example: raise in pay for a team is fixed - so declare the percentage at class level

class Team:

    pay_raise = 1.05  # 5% hike
    no_of_emps = 0  # variable that doesn't change within instance of class

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

        Team.no_of_emps +=1  # every time we create a new team instance - one employee count will be incremented

    def apply_raise(self):
        # self.pay = int(self.pay * self.pay_raise) # access clasee variables either by self / Class name itself
        self.pay = int(self.pay * Team.pay_raise)
        return self.pay


print("No of employees in team :: " + str(Team.no_of_emps))
t1 = Team('Ramesh Naik', 50000)
t2 = Team('Mohan Naik', 55000)
print(t1.apply_raise())
print(t2.apply_raise())


print("No of employees in team at the end :: " + str(Team.no_of_emps))

# why we are accessing using self.pay_raise - when it's not a instance variable?

# below 3 values are same
print(Team.pay_raise)
print(t1.pay_raise)
print(t2.pay_raise)

# but we can change it's value in instance of class if needed

print(Team.__dict__)
print(t1.__dict__)  # pay_raise variable is not available --- {'name': 'Ramesh Naik', 'pay': 52500}
print(t2.__dict__)

t1.pay_raise = 1.10 # changed to specific value

print(t1.__dict__)  # {'name': 'Ramesh Naik', 'pay': 52500, 'pay_raise': 1.1}

# *** So it's better to use self.class_variable - it gives flexibility to change it if required in instance of a class