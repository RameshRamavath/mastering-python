"""

Formal arguments - arguments in function definition

Actual arguments - arguments passed when we call the respective function

1. Position
2. Keyword
3. Default
4. Variable length  # number of arguments are not fixed

"""


def print_details(name, age):
    print("Name", name)
    print("Age", age)


# calling function

print_details(26, "Ramesh")
"""
Name 26  -- to print name, we must pass name as first argument, thus position is important
Age Ramesh
"""


# what if we don't have the access to function - but know the argument names - pass arguments as keywords

def with_keywords_print(name, age=10):
    print("Name", name)
    print("Age", age)


with_keywords_print(age=26, name="Ramesh")

"""
Name Ramesh  # with keywords - order doesn't matter
Age 26  # if nothing passed, age will be considered as 10 (default argument)
"""

"""
Variable length - number of arguments are not fixed
ex: get sum of numbers passed
"""


def add_two_numbers(x, y):
    print(x + y)


add_two_numbers(2, 3)  # 5


# add_two_numbers(2,3,5)  # TypeError: add_two_numbers() takes 2 positional arguments but 3 were given

def add_numbers(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


print(add_numbers(2, 3, 5))

"""
Keyworded variable len arguments
ex: person's info - some may provide - name, age, home place, work place 
                  - others may provide only - name, home place, work place
                  
How to accept these variable len of key word arguments - use **kwargs 
"""


def person_details(*args, **kwargs):
    print("args are :: ", args)
    print("kwargs are :: ", kwargs)


person_details(2, 3, 'Hyderabad', name='Ramesh', age=26)

# args are ::  (2, 3, 'Hyderabad') - args returns a tuple
# kwargs are ::  {'name': 'Ramesh', 'age': 26} - kwargs returns a dict

random_tuple = ('Hyd', 523328)
random_dict = {'name': 'Ramesh', 'age': 26, 'phone': '8187085500'}

person_details(*random_tuple, **random_dict)

# args are ::  ('Hyd', 523328)
# kwargs are ::  {'name': 'Ramesh', 'age': 26, 'phone': '8187085500'}
