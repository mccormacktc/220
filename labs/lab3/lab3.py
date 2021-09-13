"""
Name: Tyler McCormack
lab3.py

Problem: This lab explores loops

Certificate of Authenticity:
I certify that this is my original work.
"""

def average():
    numOfGrades = eval(input("Enter the number of grades to input"))
    acc = 0
    hw = 1
    for i in range(numOfGrades, 0, -1):
        grade = eval(input("Enter your grade on HW #" + str(hw)))
        acc = acc + grade
        hw = hw + 1
    avg = acc / numOfGrades
    print("The average grade is", avg)

def tip_jar():
    totaltips = 0
    for i in range(5):
        tip = eval(input("Enter your tip amount: "))
        totaltips = totaltips + tip
    print("The total amount of tips collected is " + str(totaltips))

def newton():
    x = eval(input("Enter the number whose square root you want to approximate"))
    approximations = eval(input("Enter the number of approximations: "))
    approx = x/2
    for i in range(approximations):
        approx = (approx + x / approx) / 2
    print("The square root of " + str(x), "is" + str(approx))

def sequence():
    numTerms = eval(input("Enter the number of terms: "))
    for x in range(1, numTerms+1):
        print(1 + x//2 * 2)

def pi():
    numPi = eval(input("Enter the number of terms for approximation of pi: "))
    acc = 1
    for x in range(numPi):
        num = 2 + ((x // 2) * 2)
        denom = 1 + (((x+1) // 2)* 2)
        frac = num/denom
        acc = acc * frac
    print(acc)

average()
tip_jar()
newton()
sequence()
pi()
