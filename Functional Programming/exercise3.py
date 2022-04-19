# Rewrite the below code using comprehensions

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []

# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list({item for item in some_list if some_list.count(item) > 1})
print(duplicates)
