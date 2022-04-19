# creating a decorator
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*' * 15)
        func(*args, **kwargs)
        print('*' * 15)
    return wrap_func

@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)

hello('Helllooooooo')
