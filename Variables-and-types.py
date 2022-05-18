
#        01010110001

# Integer, A whole number 01,010,110,001
# Binary representation of a decimal number 689
# Code e.g. area code  phone number
# List of binary states e.g. list of switches

# String, Text or numbers   ""
# Integer number 
# Floating Point Number, any fractional number
# Boolean, Either a True or False value

variable1 = "01010110001"
print(variable1)
variable2 = 1010110001
print(variable2)
variable3 = 1010110001.0
print(variable3)
variable4 = False  # Boolean 
print(variable4)


firstname = "Leon"
surname = "Robinsion"
spacechar = " "
print(firstname.upper() + " " + surname)
print(firstname.lower() + " " + surname.upper())

print(firstname.swapcase() + " " + surname)

beautyrating = 700

# Type conversion Functions

#int()  convert to Integer
#str()  convert to String
#float() convert to floating point number
#bool()  convert to a boolean

typevar1 = 25
convertvar1 = str(typevar1)
print( "This var is " + convertvar1)

convertvar2 = bool(typevar1)
print(convertvar2)

convertvar3 = float(typevar1)
print(convertvar3)

#print(firstname  + spacechar + surname + "Has a beauty rating of: "+ beautyrating )
print(f"{firstname}{spacechar}{surname} Has a beauty rating of: {beautyrating}" )

#help(int) 

# concatenate using commas and it will add spaces
str1 = "pies"
str2 = "chips"
str3 = "gravy"
print("I like: ", str1, str2, str3)
