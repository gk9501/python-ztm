# lambda expressions
from functools import reduce

my_list = [1, 2, 3]

# map with lambda
print(list(map(lambda item: item * 2, my_list)))

# filter with lambda
print(list(filter(lambda item: item % 2 != 0, my_list)))

# reduce with lambda
print(reduce(lambda acc, item: acc + item, my_list, 0))
