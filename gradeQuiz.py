import pandas as pd
from pandas import ExcelFile, ExcelWriter
import numpy as np
import re

df = pd.read_excel('/Users/rambastola/Desktop/CSC124.xlsx')
q1, q2, q3, q4, q5 = df['Question 1'],df['Question 2'],df['Question 3'],df['Question 4'],df['Question 5']


def gradeAnswers(student, correctAns, stdAns):
    print(student, correctAns, stdAns)

def studentAnswers(students, answers, quizNum, user):
    """
    get student name and quiz answers and student answers
    """
    for i in range(len(students[0])):
        if quizNum[i] == answers[user][0]:
            student = re.sub('[.]', '', students[0][i]) #removing '.' from some names
            gradeAnswers(student,answers[user],[q1[i], q2[i], q3[i], q4[i], q5[i]])

def main():
    user = int(input("Which quiz do you want to grade? ")) # which quiz to grade?
    ## TODO: check for user input. size, int

    names = df['What is (are) your name(s)?'] #student and quiz names
    quizNum = df['Which quiz are you submitting answers for?'] # all of the quiz

    quizAns=[]
    student = []
    student.append(names)
    students = np.array(student)
    for i in range(len(df.index)):
        if names[i] == "1 Correct Answer" or names[i] == "1 Answer Key":
            quizAns.append([quizNum[i], q1[i], q2[i], q3[i], q4[i], q5[i]])

    answers = np.array(quizAns)  #lists of correct quiz answers
    studentAnswers(students, answers, quizNum, user)

main()
