# a new way of formating strings in Python 3.6+

first_name = 'Ramavath'
middle_name = 'Ramesh'
last_name = 'Naik'

full_name = 'My full name is {} {} {}'.format(first_name.upper(), middle_name, last_name)
print(full_name)

# using f-string

full_name1 = f'My full name is {first_name.upper()} {middle_name} {last_name}'
print(full_name1)

person = {'first_name' : 'Ramavath', 'middle_name' : 'Ramesh', 'last_name' : 'Naik'}

full_name2 = f"My full name is {person['first_name']} {person['middle_name']} {person['last_name']}"
print(full_name2)


pi = 3.14159265

pi_vlaue = f"Pi is equal to {pi:.4f}"
print(pi_vlaue)