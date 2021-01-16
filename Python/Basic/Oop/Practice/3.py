class Animal():
    def __init__(self):
        print("Animal is on")

    def who(self):
        print("I am Animal")

    def i(self):
        print("Manthan")

class Doggy(Animal):
    def __init__(self):
        Animal.__init__(self)
        Animal.who(self)
        Animal.i(self)

myanimal = Animal()
myanimal.who()
myanimal.i()
print("\n\n")
mydog = Doggy()
