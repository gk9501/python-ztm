# This is a pure function
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list

print(multiply_by2([1, 2, 3]))

# This is not a pure function => uses print() inside it
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return print(new_list)

multiply_by2([1, 2, 3])

# This is not a pure function => uses a variable `new_list` that is outside its current scope
new_list = []
def multiply_by2(li):
    for item in li:
        new_list.append(item * 2)
    return new_list

# new_list = '' => makes the next line produce an error since new_list is acted upon using list methods in the function
print(multiply_by2([1, 2, 3]))
