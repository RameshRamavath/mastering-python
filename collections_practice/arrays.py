# In Python we can treat List as code_practice but we can't limit List to same data type elements in it

# Example List with diff data types

test_list = [1, 2, "Mahesh", 10.5]

print(test_list)
print(test_list.__class__)


# code_practice don't accept diff type of elements in it - hence we have 'array' module in Python

import array as ar
test_arr = ar.array('i', [1,2,5,7])  # array() takes at most 2 arguments - type & elements

print(test_arr)
print(test_arr.__class__)

for ele in test_arr:
    print(ele)