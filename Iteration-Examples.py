# Long form program


# Countdown Program

#startnum = 10
#print(startnum)
#startnum = startnum - 1
#print(startnum)
#startnum = startnum - 1
#print(startnum)
#startnum = startnum - 1
#print(startnum)
#startnum = startnum - 1
#print(startnum)
#startnum = startnum - 1
#print(startnum)
#startnum = startnum - 1
#print(startnum)
#startnum = startnum - 1
#print(startnum)
#startnum = startnum - 1
#print(startnum)
#startnum = startnum - 1
#print(startnum)


#  While Loop

startnum2 = 10
while startnum2 > 0:
    print(startnum2)
    startnum2 = startnum2 - 1

print("While loop Done")

# For Loop

listofnumbers = [10,9,8,7,6,5,4,3,2,1]

for i in listofnumbers:
    print(i)
print("For loop Done")


# class range(object)
# |  range(stop) -> range object
# |  range(start, stop[, step]) -> range object
# |    (negative step will count down)
# |  Return an object that produces a sequence of integers from start (inclusive)    
# |  to stop (exclusive) by step.

for loopvar in range(10,0,-3):
    print(loopvar)
print("For loop with range Done")




# iterate over a string

stringvar1 = "This is a string"
for letter in stringvar1:
    print(letter)

# iterate over a dictionary

dictionaryvar1 = {"Name":"Leon","Height":175, "Weight":83}
print(dictionaryvar1.keys())  # returns a set of the keys

for i in dictionaryvar1.keys():  # this is the same as 'for i in dictionary'
    print("the key is: " + i + " the value is: " + str(dictionaryvar1[i]))  # use the list of keys to retrieve the value


# Stopping and skipping items 

list1 = ["cats", "dogs", "mice", "sheep", "ocelots", "frogs"]

for animal in list1:
    if animal == 'sheep':
        continue  
    print(animal)  # continue will stop the iteration but continue the loop
print("Done on for loop with continue")


countvar = 10
while countvar > 0:
    if countvar == 3:
       break          # break will stop the whole loop
    print(countvar)
    countvar = countvar - 1
print("Done on while loop with break")