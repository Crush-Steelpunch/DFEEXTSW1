from abc import ABC, abstractmethod

class animal(ABC):
    weight = 80
    energy = "low"
    babies = 0

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass


class Dog(animal):
    breed = "Labrador"
    def reproduce(self):
        self.babies += 5

    def eat(self, food):
        print('yum')

class Cat(animal):
    whiskerlength = 15

class Dogwithinit:

    def __init__(self,in_breed,in_weight,in_energy):
        self.breed = in_breed
        self.weight = in_weight
        self.energy = in_energy


BilboWaggins = Dog()
chewbarka = Dog()
Clifford = Dogwithinit("Big Red Dog", 500, "High")
print(Clifford.breed)


print(chewbarka.breed)
chewbarka.breed = "West Highland Terrier"
chewbarka.weight = 40
chewbarka.energy = "High"

print(chewbarka.breed)
print(BilboWaggins.breed)
print(BilboWaggins.weight)
print(chewbarka.weight)
print(BilboWaggins.babies)
BilboWaggins.reproduce()
print(BilboWaggins.babies)



BilboWaggins.eat("dogfood")
