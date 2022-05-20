filevar = open("example.csv")
readfilevar1 = filevar.readlines()
#help(filevar)
filevar.close()

nooflines = len(readfilevar1)
for i in range(1,nooflines):
    readfilevar1[i] = readfilevar1[i].capitalize()
print(readfilevar1)
#uppercasevar = readfilevar1.lower()

#print(uppercasevar)


writevar = open("example.csv","w")
writevar.writelines(readfilevar1)
writevar.close()