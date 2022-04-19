# map, filter, zip and reduce
from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]

# map()
def multiply_by2(item):
    return item * 2

# print(map(multiply_by2, [1,2,3])) => prints where the map object is in memory
print(list(map(multiply_by2, my_list)))

# filter()
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))

# zip()
print(list(zip(my_list, your_list)))

# reduce()
def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 10))

# print(my_list, your_list) => lists are not changed since all of these are pure functions and don't have side effects
