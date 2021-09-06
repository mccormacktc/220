"""
Name: Tyler McCormack
lab2.py

Problem: Develop simple Python programs that do input, produce output, and do arithmetic.

Certificate of Authenticity:
I certify that this is my original work.
"""
import math
def sum_of_threes():
    upperbound = eval(input("Enter an upper boundary for the sum of threes."))
    acc=0
    for x in range(0, (upperbound + 1), 3):
        acc = acc + x
    print(acc)

def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l, end=" ")
        print()
def triangle_area():
    a = eval(input("Enter the length of one side of the triangle"))
    b = eval(input("Enter the length of another side of the triangle"))
    c = eval(input("Enter the length of the final side of the triangle"))
    s = (a + b + c) / 2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(A)


def sumSquares():
    lowerbound = eval(input("Enter the lower boundary"))
    upperbound = eval(input("Enter the upper boundary"))
    acc = 0
    for x in range(lowerbound, (upperbound + 1), 1):
        acc = acc + x*x
    print(acc)


def power():
    base = eval(input("Enter the base"))
    exponent = eval(input("Enter the exponent"))
    acc = 1
    for x in range(exponent):
        acc = acc * base
    print(base, "^", exponent, "=", acc)


 sum_of_threes()
 multiplication_table()
 triangle_area()
 sumSquares()
power()