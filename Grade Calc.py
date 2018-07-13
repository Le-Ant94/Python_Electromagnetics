# -*- coding: utf-8 -*-
"""

Anthony Le

This is a python program that prompts the user to input the student's
grades to calculate the average

"""

print("Please enter the student's grades, each weighted at 20%")
HW = float(input("Homework: "))

while HW > 100 or HW < 0:
    print ("Invalid input, Please enter a value between 0 and 100")
    HW = float(input("Homework: "))
    
Exam1 = float(input("Exam 1: "))

while Exam1 > 100 or Exam1 < 0:
    print ("Invalid input, Please enter a value between 0 and 100")
    Exam1 = float(input("Exam 1: "))
    
Exam2 = float(input("Exam 2: "))

while Exam2 > 100 or Exam2 < 0:
    print ("Invalid input, Please enter a value between 0 and 100")
    Exam2 = float(input("Exam 2: "))
    
Quiz = float(input("Quiz: "))

while Quiz > 100 or Quiz < 0:
    print ("Invalid input, Please enter a value between 0 and 100")
    Quiz = float(input("Quiz: "))
    
Project = float(input("Project: "))

while Project > 100 or Project < 0:
    print ("Invalid input, Please enter a value between 0 and 100")
    Project = float(input("Project: "))


def avgFunc(v, w, x, y, z):
   avr = ((v + w + x + y + z)/5)
   return avr

avg = avgFunc(HW, Exam1, Exam2, Quiz, Project)

if avg < 60:
    letter = 'F'

elif avg > 60 and avg < 70:
    letter = 'D'

elif avg > 70 and avg < 80:
    letter = 'C'

elif avg > 80 and avg < 90:
    letter = 'B'

else:
    letter = 'A'

print(" ")
print("The student's average is", round(avg, 2), "  Grade letter:", letter)

    