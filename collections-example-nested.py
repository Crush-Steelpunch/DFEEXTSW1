# Create a new Python file and write a program that does the following:
#
#    Asks for an input from the user as a mark. 
#        - what do I know that asks for input
#               Input function

#    If the mark is greater that 85 print "Distinction"  - DONE
#       What do I know that a) does tests b) does output?
#                           if statement      print function

#    If the mark is between 65 and 85 print "Pass"  -  DONE
#    Anything else print "Fail"   - DONE
#
#Try to do this both with and without elif statements.

markvar1 = int(input("Input your mark: "))

if markvar1 > 85:
    print("Distinction")
else:
    if markvar1 < 65:
        print("Fail")
    else:
        print("Pass")
