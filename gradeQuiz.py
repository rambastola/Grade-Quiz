import pandas as pd
from pandas import ExcelFile, ExcelWriter
import numpy as np
import re

df = pd.read_excel('/Users/rambastola/Desktop/CSC124.xlsx')
q1, q2, q3, q4, q5 = df['Question 1'],df['Question 2'],df['Question 3'],df['Question 4'],df['Question 5']

def grade(student, soloPoints):
    s = []
    s.append(student)
    print(s)


def studentAnswers(students, correctAns, quizNum, user):
    """
    students: all the student
    correctAns: all quizes answers
    quizNum: all the quizes classification
    user: int. classification of the quiz to be graded
    """
    for i in range(len(students[0])):
        if quizNum[i] == correctAns[user][0]: #choose the correct set of answers
            student = re.sub('[.]', '', students[0][i]) #removing '.' from some names
            evalAnswers(student,correctAns[user],[q1[i], q2[i], q3[i], q4[i], q5[i]])

def evalAnswers(student, correctAns, stdAns):
    """
    student: str of students
    correctAns: array of correct answers
    stdAns: Student answers
    """

    soloPoints = 0
    groupPoints = 0
    # for name in args:


    if student.count(',') == 1: #single quiz. up to 10 points
        if correctAns[1] == stdAns[0]:
            soloPoints +=2
        if correctAns[2] == stdAns[1]:
            soloPoints +=2
        if correctAns[3] == stdAns[2]:
            soloPoints +=2
        if correctAns[4] == stdAns[3]:
            soloPoints +=2
        if correctAns[5] == stdAns[4]:
            soloPoints +=2

    elif student.count(',') > 1: #group quiz. up to 5 points
        if correctAns[1] == stdAns[0]:
            groupPoints +=1
        if correctAns[2] == stdAns[1]:
            groupPoints +=1
        if correctAns[3] == stdAns[2]:
            groupPoints +=1
        if correctAns[4] == stdAns[3]:
            groupPoints +=1
        if correctAns[5] == stdAns[4]:
            groupPoints +=1
    grade(student, soloPoints, )


def main():
    user = int(input("Which quiz do you want to grade? ")) # which quiz to grade?
    ## TODO: check for user input. size, int

    names = df['What is (are) your name(s)?'] #student and quiz names
    quizNum = df['Which quiz are you submitting answers for?'] # all of the quiz

    quizAns=[]
    student = [names]
    students = np.array(student)
    for i in range(len(df.index)):
        if names[i] == "1 Correct Answer" or names[i] == "1 Answer Key":
            quizAns.append([quizNum[i], q1[i], q2[i], q3[i], q4[i], q5[i]])

    correctAns = np.array(quizAns)  #lists of correct quiz answers
    studentAnswers(students, correctAns, quizNum, user)

main()
