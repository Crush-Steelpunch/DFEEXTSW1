animallistvar = []
while not "cat" in animallistvar:
    typedinvar = input("Type in an animal: ")
    animallistvar.append(typedinvar)

print(animallistvar)
print("Oh no, a cat appeared!")