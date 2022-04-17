class User():
    def sign_in(self):
        print('logged in')

    def attack(self): # this is overriden if the subclass has an attack method of its own
        print('do nothing')

# Sub-classes
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

# print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User)) # prints True because wizard1 is created from the Wizard class, which is a subclass of User

# example of polymorphism
# although both classes share the same method name of `attack`, they produce different output
wizard1.attack()
archer1.attack()

# Representation 1
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

# Representation 2
# for char in [wizard1, archer1]:
#     char.attack()
