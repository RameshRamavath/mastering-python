# *********************** List ***********************

courses = ['Telugu', 'Hindi', 'English', 'Arts', 'Math']
print( courses[1] ) # get element by index
print( courses[-1])
print( courses[-5], courses[0])

print( courses.__getitem__(1) ) # another way to get items
print( len(courses))  # size of list

# ******* slicing lists *******

print( courses[0:3])  # starting from zero index - upto index 3 (index 3 is not inclusive)
print( courses[:3])
print( courses[3:])

# ****** updating list  *******

courses.append('Physics')    # at the end append
courses.insert(0, 'Social')  # at specific index

print( courses)

#  ******* add list of elements to existing list *******

courses_2 = ['Python', 'Java']
# courses.insert(0, courses_2)

print( courses) # [['Python', 'Java'], 'Social', 'Telugu', 'Hindi', 'English', 'Arts', 'Math', 'Physics']

# instead use extend() method

courses.extend(courses_2)  # appended list elements at the end
print( courses) # ['Social', 'Telugu', 'Hindi', 'English', 'Arts', 'Math', 'Physics', 'Python', 'Java']

# ******* remove elements from list *******

courses.remove('Social')
print( courses)
courses.pop()  # to remove element from top  - Use this method if you want to use list as queue or stack
print( courses)
print( courses.pop() )# u can store the value we popped

# ******* Sorting of elements *******

courses.sort() # sorting in place
print( courses)

sorted_courses = sorted(courses)  # don't change the original list
print( sorted_courses)

# *******  getting index of particular element *******

print( courses.index('Arts'))
# print( courses.index('Python')  # ValueError: 'Python' is not in list

# instead use 'in' operator for checking for specific item in list

print( 'Arts' in courses)   # True
print( 'Python' in courses)  # False

# ******** looping through the elements ********

for course in courses:
    print( "current course is : ", course)

for index, course in enumerate(courses):  # if we want to get the index also use enumerate
    print( "currently we are at index {} and course is : {}".format(index, course))



# *********************** Tuple ***********************

''' 
  Similar to List but Tuples are not mutable
'''

course_new = ['Math', 'Physics']
course_new[0] = 'Maths Paper2'
print( course_new) # list is updated

course_tuple = ('Math', 'Physics')
# course_tuple[0] = 'Maths Paper2'   # TypeError: 'tuple' object does not support item assignment
print( course_tuple)# Tuple can't be updated


# *********************** Set ***********************

''' 
  Similar to List but un-ordered and duplicates are not allowed 
  
'''

course_set = {'Math', 'Physics', 'Math'} # we will have Math only once - removes duplicate
empty_set = set()
empty_set.add(1)
empty_set.update({2,3,4,5})

print( course_set)
print( empty_set)


# *********************** Dictionaries ***********************
''' 
  Working with key-value pairs in Python 
  
'''

student = {'name': 'Ramesh', 'place': 'Hyd', 'age': 26, 'courses': ['Math', 'Physics']}
print( student)

print( student['name']) # get value of a key
# print( student['emial']  # KeyError: 'emial'

# so getting key value error is not good practice  - so use get method

print( student.get('name'))
print( student.get('emial') ) # None
print( student.get('Phone', 'Not found') )# can give default value instead of getting None

# **** Update the elements ****

student['name'] = 'Mahesh' # update existing element
student['phone'] = '8187085549' # add new element

print( student)  # {'courses': ['Math', 'Physics'], 'age': 26, 'place': 'Hyd', 'name': 'Mahesh', 'phone': '8187085549'}

# do all in one go - use update()  method

student.update({'name': 'Ramesh', 'age':27, 'phone': '55-66-100'})
print( student) # {'name': 'Ramesh', 'phone': '55-66-100', 'age': 27, 'courses': ['Math', 'Physics'], 'place': 'Hyd'}

# delete elements

del student['age']
print( student)
print( "length of dict : ", len(student))

print( "keys in student dict : ", student.keys())
print( "value in student dict : ", student.values())
print( "keys & value tuples : ", student.items())

# Iterations

for key, value in student.items():
    print( "key: {}, value: {}".format(key, value))


