"""

lists are iterable but not iterators - what's the difference?

when we able to loop through a collection or object we call it iterable.
when a class/method/collection has  __iter__ and __next__ dunder methods - we generally call it iterator

"""

list1 = [1, 2, 3, 4]
for num in list1:
    print(num)  # because its iterable


# print(next(list1))  # TypeError: 'list' object is not an iterator

# write a class implementing iterable

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)

# print("values from implemented class")
# for num in nums:
#     print(num)


# we can use next method to get one number at a time
print("** Using next method **")
print(next(nums))
print(next(nums))


# generator methods does the same without dunder methods like __iter__ and __next__

# let's write one generator which does same thing - generator creates dunder methods automatically

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


range_nums = my_range(10, 15)
print("Printing numbers from decorators")
print(next(range_nums))
print(next(range_nums))
print(next(range_nums))

print("Looping from decorators")

for num in range_nums:
    print(num)
