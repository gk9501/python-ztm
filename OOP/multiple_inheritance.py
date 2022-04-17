class User():
    def sign_in(self):
        print('Logged in')

# Sub-classes
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking using magic with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'Arrows - {self.arrows} remaining')

    def run(self):
        print('Ran really fast')

class HybirdBorg(Wizard, Archer): # Multiple inheritance
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybirdBorg('Talos', 50, 100)
hb1.sign_in()
hb1.run()
hb1.check_arrows()
hb1.attack()
