# list comprehensions
# my_list = []

# for char in 'hello':
#     my_list.append(char)

my_list1 = [char for char in 'hello']                       # doing the same as the above using list comprehensions
my_list2 = [num for num in range(100)]                      # list of numbers 0 to 99
my_list3 = [num ** 2 for num in range(100)]                 # list of squares of numbers 0 to 99
my_list4 = [num ** 2 for num in range(100) if num % 2 == 0] # list of even squares of numbers 0 to 99

print(my_list4)

# set comprehensions
my_set1 = {char for char in 'hello'}
my_set2 = {num for num in range(100)}
my_set3 = {num ** 2 for num in range(100)}
my_set4 = {num ** 2 for num in range(100) if num % 2 == 0}

print(my_set4)

# dictionary comprehensions
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict1 = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0}
my_dict2 = {num:num*2 for num in [1,2,3]}

print(my_dict2)
