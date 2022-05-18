# A Function that will test if a string is a palendrome

def palindrometest(instring):
    backwards = ''
    strlen = len(instring)-1
    while strlen > -1:
        backwards = backwards + instring[strlen]
        strlen -= 1
    
    if backwards == instring:
        return True
    else:
        return False

print(palindrometest("racecar"))