name = input( "students name :")
homeworkscore = int(input ("students homework score :"))
assessmentsceor =int(input("students assessment score:" ))
finalexamscore = int(input("students final exam score :"))
sumcore = ((homeworkscore+ assessmentsceor +finalexamscore)/175 ) * 100
print("Your percentage is " + str(sumcore) + "%")
# individual percentages 

homeworkscore = (homeworkscore/25)*100
print("homework percentage was " + str(homeworkscore) + "%")
assessmentsceor = ((assessmentsceor*50)/sumcore)*100
finalexamscore = (finalexamscore/sumcore)*100

def get_letter_ICTgrade(Final_Score):
    if Final_Score>=70 and Final_Score<=100:
        greade = "A"
    elif Final_Score>=69 and Final_Score<=50:
        greade = "B"
    elif Final_Score>=49 and Final_Score<=40:
        greade = "C"
    else:
        greade = "D"
    return greade

print("%sICT grade:%.2f"%(name,ICT grade))