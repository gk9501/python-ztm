class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return self.color

    def __len__(self):
        return 5

    def __call__(self):
        return 'yess?'

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__()) # does the same thing as print(str(action_figure))
print(len(action_figure)) # __len__
print(action_figure()) # __call__
print(action_figure['name']) # __getitem__
