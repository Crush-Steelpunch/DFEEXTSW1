import pdb
pdb.set_trace()
# Example written by Dee

def grade_calc(hw_score, asment_score, exam_score):
    hw_score_int = int(hw_score)
    asment_score_int = int(asment_score)
    exam_score_int = int(exam_score)
    final_ict_grade = float((hw_score_int + asment_score_int + exam_score_int)/175)
    final_ict_grade_percent = "{:.0%}".format(final_ict_grade)
    return final_ict_grade_percent

name_1 = str(input("What is yoyur name?: "))
hw_score_1 = int(input("What is your homework score?: "))
asment_score_1 = int(input("What is your assmessment score?: "))
exam_score_1 = int(input("What is your exam score?: "))

grade_calc_1 = grade_calc(hw_score_1, asment_score_1, exam_score_1)

print(f"Your name is: {name_1} and your score is {grade_calc_1}")