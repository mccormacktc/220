"""
Name: Tyler McCormack
template.py

Problem: This is a template for all future code

Certificate of Authenticity:
I certify that this is my original work.
"""

## 1: The program will intake a set of numbers and output the RMS Average,
# Harmonic Mean, and Geometric Mean
## 2: The input will be a set of numbers, and the output will be the set's RMS Average,
# Harmonic Mean, and Geometric Mean
## 3: a. prompt user for the number of numbers inputted
##    b. ask for numbers
##    c. compute arithmetic mean, RMS average, harmonic mean, and geometric mean
from math import sqrt

def main():
    amount_nums = eval(input("How many values would you like to enter?"))
    sum_nums2 = 0
    harmonic_denom = 0
    geometric_under = 1
    for _ in range(amount_nums):
        num = eval(input("Enter value:"))
        sum_nums2 = sum_nums2 + num ** 2
        harmonic_denom = harmonic_denom + (1 / num)
        geometric_under = geometric_under * num
    rms_average = sqrt(sum_nums2 / amount_nums)
    harmonic_mean = amount_nums / harmonic_denom
    geometric_mean = geometric_under ** (1/amount_nums)
    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))
if __name__ == '__main__':
    main()
