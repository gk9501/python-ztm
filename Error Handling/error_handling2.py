def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err: # returns an error object
        print(err)

# print(sum('1', 2))

def div(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError): # handles both errors the same way
        print('ooops')

print(div('1', 2))
print(div(1, 0))
