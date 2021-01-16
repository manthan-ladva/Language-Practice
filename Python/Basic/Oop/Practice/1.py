class Dog():
    species = "Dog"
    def __init__(self, breed, name):
        print("I am in class")
        self.bre = breed
        self.name = name
manthan = Dog("Husky", "Tom")
print(manthan.bre)
print(manthan.name)
