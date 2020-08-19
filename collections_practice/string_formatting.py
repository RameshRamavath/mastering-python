# from person dict - print( person name and age

person = {'name': 'Ramesh', 'age': 26}

msg = "My name is " + person['name'] + " and I am " + str(person['age']) + " years old."
# we need take of white-spaces and too much string concatination
print( msg)

# better to use formatting option

msg2 = "My name is {} and I am {} years old.".format(person['name'], person['age'])
print( msg2)

msg3 = "My name is {0} and I am {1} years old.".format(person['name'], person['age'])
print( msg3)

# pass the keys in parenthesis and collection name in format

msg4 = "My name is {0[name]} and I am {0[age]} years old.".format(person)
print( msg4)

# use as keyword arguments

msg5 = "My name is {name} and I am {age} years old.".format(**person)
print( "msg5 :: " + msg5)

# **** Grab values from Class instance ***

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

# create person instance

p1 = Person('Mahesh', '30')

sentence = "My name is {0.name} and I am {0.age} years old.".format(p1)
print( sentence + " *** From class")


# formatting float values to certain decimal places

pi = 3.14159265

pi_vlaue = "Pi is equal to {:.3f}".format(pi) # 3 decimal places
print( pi_vlaue)

# formatting large number with comma separated

mb_value = '1 MB is equal to {:,.2f} bytes'.format(1000**2)  # .2f for decimal points
print( mb_value)

# formatting dates in required format

import datetime
my_date = datetime.datetime(2020, 8, 19, 5, 45, 12)
print( "original date : " + str(my_date))

# format the date to -> August 19, 2020

date_formatted = '{:%B %d, %Y}'.format(my_date)
print( date_formatted)