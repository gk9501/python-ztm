# Create a class named `SuperList`, and add code that allows us to use it just like a regular list in Python.
# The only difference is that SuperList must have a special __len__() method, which should return 1000 everytime.

class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
