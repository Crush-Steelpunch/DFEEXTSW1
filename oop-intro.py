# string object

stringvar1 = "aeiou"

print(stringvar1.upper())

# A Class is an Object

# Class data - attributes
# Class functions - methods 
# 
# Attributes of object Dog
class Dog:
  Breed = "Breed"
  Weight = 0
  Energy = "Low"

BilboWaggins = Dog()

chewbarka = Dog()
chewbarka.Breed = "Scotty"
chewbarka.Weight = 40
chewbarka.Energy = "High"

print(BilboWaggins.Breed)
print(BilboWaggins.Weight)
print(BilboWaggins.Energy)

print(chewbarka.Breed)
print(chewbarka.Weight)
print(chewbarka.Energy)