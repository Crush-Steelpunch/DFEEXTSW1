filevar1 = open("example.csv","r")
print(filevar1.read()) # This creates a string
filevar1.close()

filevar1 = open("example.csv","r")
print(filevar1.readlines()) # This creates a list
filevar1.close()


filevar1 = open("example.csv","a") # this allows you to append to the file
filevar1.close()

filevar1 = open("example.csv","w") # this removes the data in the file before writing new data
filevar1.close()