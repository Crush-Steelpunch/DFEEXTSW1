def animaltesting(variable):
    if variable == "cat":
        return True
    else:
        return False




returnval = False
while not returnval:
    typedinvar = input("Type in an animal: ")
    returnval = animaltesting(typedinvar)

print("Oh no, a cat appeared!")