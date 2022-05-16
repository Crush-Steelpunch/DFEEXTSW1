firstname = "Leon"
surname = "Robinson"
height = 175
weight = 83
happinesgrade = "q"
payscale = "9000andabit"

# Lists

leondatavar = ["Leon", "Robinson", 175, 83, "q", "9000andabit"]
print(leondatavar)
richarddatavar = ["Richard", "Mansworth", 190, 85, "q", "9000andalot"]
earldatavar = ["Earl", "Grey", 165, 80, "q", "9000andthatsit"]
print(leondatavar[2])

stafflistdatavar = [ leondatavar, richarddatavar, earldatavar ]
print(stafflistdatavar[2][1])

leondatavar.append("Black Polo Tshirt")
print(leondatavar)
leondatavar.remove("q")
print(leondatavar)
leondatavar.insert(1, "L")
print(leondatavar)

leondatavar[5] = "Landthensome"
print(leondatavar)

# Tuple


richardtuplevar = ("Richard", "Mansworth", 190, 85, "q", "9000andalot")
# richardtuplevar[1] = "Pondsworth"  # This isn't allowed
print(richardtuplevar)

firstname = richardtuplevar[0]
surname = richardtuplevar[1]
height = richardtuplevar[2]
firstname, surname, height, weight, happinesgrade, payscale = richardtuplevar
print(happinesgrade)



# Strings are like Tuples

stringvar1 = "I like pies"
print(stringvar1[2:6])


# Dictionary

leondatadict = { "firstname": "Leon", "surname":"Robinson", "height":175, "weight":83, "happinessgrade":"q","payscale":"9000andabit" }
richarddatadict = { "firstname": "Richard", "surname":"Mansworth", "height":185, "weight":80, "happinessgrade":"q","payscale":"9000andabit" }
print(leondatadict["height"])
print(richarddatadict["height"])

richarddatadict["colour"] = "blue" # 'append' to a dictionary
print(richarddatadict)
richarddatadict["happinessgrade"] = "X"
print(richarddatadict)


inputvar1 = input("Type either cheese or wine: ")
foodsdict = {"cheese": ["cheddar", "mozerella", "brie", "lancashire"], "wine": ["shiraz", "Merlot", "rose"]}
list1 = foodsdict[inputvar1]

print("You picked " + inputvar1 + " which contains:" + ", ".join(list1))