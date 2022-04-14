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

    def run(self, hello):
        print(hello)

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50  # adds an attack attribute to player2

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)
print(player1.shout())
print(player2.membership)
print(player1.run("Hello!"))
