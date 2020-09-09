import itertools

#  ******* count() ********

counter = itertools.count(start=5, step=2)

# use next method to start counting

print(next(counter))
print(next(counter))
print(next(counter))

# use count method to assign indexes to elements in list

data = [100, 200, 300, 400, 500]
data_count = zip(itertools.count(), data)  # zip - pairs two tuples together
print(list(data_count))  # [(0, 100), (1, 200), (2, 300), (3, 400), (4, 500)]

tuple1 = (1, 2, 3)
tuple2 = (11, 12, 13, 14)
print(list(zip(tuple1, tuple2)))  # [(1, 11), (2, 12), (3, 13)]

#  ******* zip_longest() ********
# when one tuple is exahusted, it won't zip other values from logest tuple
# use zip_longest method here

print(list(itertools.zip_longest(tuple1, tuple2, fillvalue='NA')))  # [(1, 11), (2, 12), (3, 13), (None, 14)]

#  ******* cycle() ********
# it goes over the collection again and again

cycle_data = [1000, 2000, 3000]
cycle_counter = itertools.cycle(cycle_data)
print(next(cycle_counter))
print(next(cycle_counter))
print(next(cycle_counter))
print(next(cycle_counter))
print(next(cycle_counter))

# *** combinations, permutations and product ***

letters = ['a', 'b', 'c']
comb = itertools.combinations(letters, r=2)  # combination of two letters
print("combinations are ::: ", list(comb))  # order doesn't matter -->  [('a', 'b'), ('a', 'c'), ('b', 'c')]
print("permutations are ::: ", list(
    itertools.permutations(letters, r=2)))  # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

numbers = [1, 2, 3]
# print the combinations with repetitions
print("product ::: ", list(itertools.product(numbers, repeat=3)))  # password checker with all possible combinations


# *** chain ***
# chain multiple iterables to traverse all of them

names = ['Ramesh', 'Naik']

"""
to iterate over letters, numbers and names - we can do 

final_list =  letters + numbers + names   ==> but we are storing all the data in memory again - to avoid this use chain

for item in final_list:
    print(item)

"""

combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)

"""
Slicing on iterator - islice(collection, stoping_point)
"""

result = itertools.islice(range(10), 5)
for item in result:
    print("islice item : ", item)

result2 = itertools.islice(range(10), 1, 5)  # starting and ending point, can be added step at the end
for item in result2:
    print("islice ex2 : ", item)

"""
compress - filter elements matching data with selectors
"""

selectors = [True, False, True, True]
data_com = ['a', 'b', 'c', 'd']
result_com = itertools.compress(data_com, selectors)  # (data, selectors)

for item in result_com:
    print(item)