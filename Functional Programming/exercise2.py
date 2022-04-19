# Write a lambda expression that squares all the numbers in `my_list`
my_list = [5, 4, 3]
print(list(map(lambda num: num ** 2, my_list)))

# Sort `a` in ascending order based on the second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
