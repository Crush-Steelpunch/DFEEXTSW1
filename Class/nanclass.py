class Student:
    test_Scores = 0
    def __init__(self,name, age,Class="student"):
        self.name = name
        self.age = age
        self.Class = Class

# It should also contain a method which takes in 3 test scores 
# and prints the students average test score.
# method - DONE - nan
# 3 scores - DONE - leon
# prints - DONE  - nan
# average test score - maths, which average?   - DONE  - leon
#           mean avg   - add up all numbers and divide by count

    def test_Scores(self, score1,score2,score3):
        # calculate mean averag
        self.test_Scores = (score1 + score2 + score3) / 3
        print(self.test_Scores)

jessa = Student("Peter",14)   # - nan
print(jessa.name + " " + str(jessa.age) + " " + jessa.Class)  # leon
#Student.test_Scores("ENglish,Tom")
jessa.test_Scores(10,14,17)  # leon