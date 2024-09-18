class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal): #subclass
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

animale = Animal("Bobby", "white")
print("Colore dell'animale -> " + animale.color)

fido = Dog("Fido", "brown")
fido.bark()