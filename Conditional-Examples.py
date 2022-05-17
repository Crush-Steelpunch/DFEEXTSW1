# Selection is: if this then that

inputvar1 = bool(int(input("Please type a 1 or 0: ")))
#print(type(inputvar1))
#print(inputvar1)
if inputvar1:
    print("The test was True")
else:
    print("The test was False")
print("this line will always print")

inputvar2 = int(input("Please enter a number between 1 and 100: "))
if inputvar2 > 90:
    print(str(inputvar2) + " is greater than 90")
elif  inputvar2 > 75:
    print(str(inputvar2) + " is greater than 75")
elif inputvar2 == 75:
    print(str(inputvar2) + " is equal to 75")
elif inputvar2 > 50:
    print(str(inputvar2) + " is greater than 50")
else:
    print(str(inputvar2) + " is less than or equal to 50")
print("Done")



inputvar3 = int(input("Please type a number between 1 and 100: "))
if inputvar1 > 50:
    if inputvar1 > 90:
        print("Input was greater than 90")
    else:
        print("Input was greater than 50 but less than or equal to 90")
else:
    print("Input was less than 50")
print("Done")


inputvar4 = int(input("Type a number: "))

if inputvar4 < 50 and inputvar4 > 0:
    print("Input is less than 50 and not negative")
else:
    if inputvar4 > 50:
        print("Bignum!")
    else:
        print("Negative number")
print("done")


inputvar5 = int(input("Type a number positive or negative "))
if inputvar5 < 99 and not inputvar5 < 0 :
    print("It was positive and less than 90")
else:
    if not inputvar5 < 0:
        print("Positive")
    else:
        print("negative")
