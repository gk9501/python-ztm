class PlayerCharacter:
    membership = True # Class Object Attribute
    def __init__(self, name='anonymous', age=0):
        # We can do this to refer to `membership` => if PlayerCharacter.membership:
        # or do this => if self.membership:
        if age > 18: # the attributes are only initialised if age > 18
            self.name = name # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2): # `cls` is the class that is taken as a parameter
        return cls("Orion", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2): # `cls` is not taken as a parameter here
        return num1 + num2

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50  # adds an attack attribute to player2

# print(PlayerCharacter.adding_things(2, 3)) => this is done to access methods with the @classmethod decorator
player3 = PlayerCharacter.adding_things(10, 9)
print(player3.age)

# print(player1.name)
# print(player1.age)
# print(player2.name)
# print(player2.age)
# print(player1.shout())
# print(player2.membership)
# print(player1.run("Hello!"))
