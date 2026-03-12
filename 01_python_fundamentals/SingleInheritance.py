class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def makeSound(self):
        print("Sound made by the animals.")
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def makeSound(self):
        print("Bark")

d=Dog("Dog","German")
d.makeSound()

a=Animal("Dog","Golden")
a.makeSound()