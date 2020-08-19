# List comprehensions - Easy way to create list's in Python

# create copy of list using for loop

nums = [1, 2, 3, 4, 5]

# print nums
#
# new_list = []
# for num in nums:
#     new_list.append(num)
# print new_list

# list comprehension version

new_list = [n for n in nums] # [ n (output for each iter) for n (each element) in nums (our list)]
print(new_list)

# create list of squares

# squared_list = []
# for num in nums:
#     squared_list.append(num * num)
# print squared_list

squared_list = [n*n for n in nums]
print(squared_list)

# using map and lambda (unanimous func) function

lam_list = map(lambda n: n*n, nums) # map applies any function on each element of a collection
print(lam_list)

# get even numbers from list

# using lambda
even_list = filter( lambda n: n%2 ==0, nums)
print(even_list)

# using for loop
even_list2 = []
for num in nums:
    if num%2 ==0:
        even_list2.append(num)
print(even_list2)

# using list comprehension

even_list3 = [n for n in nums if n%2 == 0]
#print even_list3

# return (letter, num) for each letter in 'abcd' and '0123'

num_list = []
for letter in 'abcd':
    for num in range(4):
        num_list.append((letter, num))

#print num_list

# using comprehensions

num_list1 = [(letter, num) for letter in 'abcd' for num in range(4)]
#print num_list1

####### Dict comprehensions ######

names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']

print(zip(names, heros))  # gives list of tuples

# get dict from tuple

my_dict = {}
for key, value in zip(names, heros):
    my_dict[key] = value

print(my_dict)

# comprehension

my_dict2 = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict2)

## Set comprehension

list2 = [1,1,2,2,3,3,4,5]
my_set = {n for n in list2}
print(my_set)   # set([1, 2, 3, 4, 5])




