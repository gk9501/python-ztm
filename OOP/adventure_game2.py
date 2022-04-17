class User():
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email) # calls the __init__ method of the User class to give the Wizard class the email attribute
        super().__init__(email) # cleaner method of doing the same as the above line
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
print(wizard1.email) # produces an error if __init__ method of Wizard class is different from that of the parent User class
print(dir(wizard1))
