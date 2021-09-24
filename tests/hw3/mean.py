"""
Name: Tyler McCormack
template.py

Problem: This is a template for all future code

Certificate of Authenticity:
I certify that this is my original work.
"""

## 1: The program will intake a set of numbers and output the RMS Average, Harmonic Mean, and Geometric Mean
## 2: The input will be a set of numbers, and the output will be the set's RMS Average, Harmonic Mean, and Geometric Mean
## 3: a. prompt user for the number of numbers inputted
##    b. ask for numbers
##    c. compute arithmetic mean, RMS average, harmonic mean, and geometric mean
from math import sqrt

def main():
    amountNums = eval(input("How many values would you like to enter?"))
    sumOfNums2 = 0
    harmonicDenom = 0
    geometricUnder = 1
    for i in range(amountNums):
        num = eval(input("Enter value:"))
        sumOfNums2 = sumOfNums2 + num ** 2
        harmonicDenom = harmonicDenom + (1 / num)
        geometricUnder = geometricUnder * num
    rms_average = sqrt(sumOfNums2 / amountNums)
    harmonic_mean = amountNums / harmonicDenom
    geometricMean = geometricUnder ** (1/amountNums)
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometricMean, 3))
if __name__ == '__main__':
    main()