def animaltesting(variable):
    if variable == "cat":
        return False 
    else:
        return True




returnval = True
while returnval:
    typedinvar = input("Type in an animal: ")
    returnval = animaltesting(typedinvar)

print("Oh no, a cat appeared!")