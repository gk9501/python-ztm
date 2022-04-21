# creating a generator
def generator_function(num):
    for i in range(num):
        yield i * 2

g = generator_function(100)
next(g)
next(g)
print(next(g)) # prints 4

# for item in generator_function(1000000):
#     print(item)

# def make_list(num):
#     result = []
#     for i in range(num): # unlike a list, range() creates items one by one, not all at once
#         result.append(i * 2)
#     return result

# my_list = make_list(100)
# print(list(range(1000000)))
