import pandas as pd
from pandas import ExcelFile, ExcelWriter
import numpy as np
import re

df = pd.read_excel('/Users/rambastola/Desktop/CSC124.xlsx')
q1, q2, q3, q4, q5 = df['Question 1'],df['Question 2'],df['Question 3'],df['Question 4'],df['Question 5']

def grade(solo, group):
    """
    solo: dict of single student name and their score
    group: dict of multi-std names and score
    """

    official = {}
    for key, value in solo.items():
        for k, v in group.items():
            if key in k:
                gp = group[k]
                official[key] = gp + solo[key]

    print(official)


def studentAnswers(students, correctAns, quizNum, user):
    """
    students: all the student
    correctAns: all quizes answers
    quizNum: all the quizes classification
    user: int. classification of the quiz to be graded
    """

    soloPoints = 0
    groupPoints = 0

    solo = {}
    group= {}

    for i in range(len(students[0])):
        if quizNum[i] == correctAns[user][0]: #choose the correct set of answers
            student = re.sub('[.]', '', students[0][i]) #removing '.' from some names

            if student.count(',') == 1: #single quiz. up to 10 points
                if correctAns[user][1] == q1[i]:
                    soloPoints +=2
                if correctAns[user][2] == q2[i]:
                    soloPoints +=2
                if correctAns[user][3] == q3[i]:
                    soloPoints +=2
                if correctAns[user][4] == q4[i]:
                    soloPoints +=2
                if correctAns[user][5] == q5[i]:
                    soloPoints +=2

                solo[student] =soloPoints
                soloPoints = 0

            elif student.count(',') > 1: #group quiz. up to 5 points
                if correctAns[user][1] == q1[i]:
                    groupPoints +=1
                if correctAns[user][2] == q2[i]:
                    groupPoints +=1
                if correctAns[user][3] == q3[i]:
                    groupPoints +=1
                if correctAns[user][4] == q4[i]:
                    groupPoints +=1
                if correctAns[user][5] == q5[i]:
                    groupPoints +=1

                group[student] =groupPoints
                groupPoints = 0
    grade(solo, group)


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
