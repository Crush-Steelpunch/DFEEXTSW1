def animaltesting(variable):
    if variable == "cat":
        return False 
    else:
        return True

def add1(userinputvar):
    useroutputvar = userinputvar + 1
    # print(userinputvar)
    return useroutputvar


def sorted():
    return "Leon is sorted, nice one!"

def unknownlenght(*varname):
    # the varname creates a tuple
    countlist = len(varname)
    return (varname, countlist)