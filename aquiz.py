# Quiz
import time
import sys
# Questions

# Lists that will put the questions in them 
correctquestions = []
wrongquestions = []

def q1():
    print("What is 1+1")
    A = print("A. 6")
    B = print("B. 5")
    C = print("C. 2")
    D = print("D. 4")
    question = input("Answer: ").upper()
    if question == 'C':
        correctquestions.append("Question 1")
    else: 
        wrongquestions.append("Question 1")
def q2():
    print("What is the capital of the United States")
    A = print("A. Turkey")
    B = print("B. Phoenix")
    C = print("C. Washington DC")
    D = print("D. Seattle")
    question = input("Answer: ").upper()
    if question == 'C':
        correctquestions.append("Question 2")
    else:
        wrongquestions.append("Question 2")
def q3():
    print("What country borders the USA to the North")
    A = print("A. Meixco")
    B = print("B. Canada")
    C = print("C. Cuba")
    D = print("D. Florida")
    question = input("Answer: ").upper()
    if question == 'B':
        correctquestions.append("Question 3")
    else: 
        wrongquestions.append("Question 3")
def q4():
    print("What is the name of a animal with fur")
    A = print("A. Mamal")
    B = print("B. Fish")
    C = print("C. Bird")
    D = print("D. None of the above")
    question = input("Answer: ").upper()
    if question == 'A': 
        correctquestions.append("Question 4")
    else:
        wrongquestions.append("Question 4")

q1()
q2()
q3()
q4()

# Testing to see if the questions go into the correct list

print(wrongquestions)
print(correctquestions)

# Calculate score 
def calculation(): 
    totalquestions = 4 
    numberofwrong = len(wrongquestions)
    math = numberofwrong / totalquestions
    calc = ((math * 100))
    mathmatics = int(calc)
    print(f'You got a {mathmatics}% on the quiz!')

# Goes again if user would like to try the test again to get a better score
def tryagain():
    again = input("Would you like to try again?").upper()
    if again == 'Y':
        print("Ok!")
        time.sleep(2)
        q1()
        q2()
        q3()
        q4()
        calculation()
        tryagain()
    else: 
        print("Ok!")
        time.sleep(2)
        sys.exit()

calculation()
tryagain()