# how to create class, how to create object from it
# how to assign values to member variables of Class


class Employee:
    # Class objects support two kinds of operations: attribute references and instantiation
    # name and age - attributes / Instance variables
    # instantiation - __init__ [similar to constructor in Java]

    # class variables  - same for all instances / shared by all instances
    company = "Western Union"

    def __init__(self, name, age):
        self.emp_name = name
        self.emp_age = age


if __name__ == '__main__':
    emp1 = Employee("Ramesh", 26)

    # Every class will have default constructor / instantiation method - then assign values to member attributes
    emp2 = Employee
    emp2.emp_name = "mahesh"
    emp2.emp_age = 30

    print "Employee 1 name - {} and Company - {}".format(emp1.emp_name, emp1.company)
    print "Employee 2 name - {} and Company - {}".format(emp2.emp_name, emp2.company)


