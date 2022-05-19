class Dog:
    breed = "Labrador"
    weight = 80
    energy = "Low"


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