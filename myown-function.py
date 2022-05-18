def add1(userinputvar):
    useroutputvar = userinputvar + 1
    # print(userinputvar)
    return useroutputvar

def staffstats(staffname:str,staffweight:int=81):
    uppername = staffname.upper()
    if staffweight%5 == 0:
        result = True
    else:
        result = False
    return [uppername,result]


inputnum = 7
inputnum2 = 16

functionoutvar = add1(inputnum)

print(functionoutvar)

functionoutvar1 = add1(inputnum2)
print(functionoutvar1)


leondatavar = ["Leon", "Robinson", 175, 83, "q", "9000andabit"]
richarddatavar = ["Richard", "Mansworth", 190, '' , "q", "9000andalot"]
earldatavar = ["Earl", "Grey", 165, 80, "q", "9000andthatsit"]


print(staffstats(leondatavar[1], leondatavar[3]))
print(staffstats(richarddatavar[1],7))
print(staffstats(earldatavar[1], earldatavar[3]))

