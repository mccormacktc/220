"""
Name: Tyler McCormack
lab9.py

Problem: Lab 9

Certificate of Authenticity:
I certify that this is my original work.
"""
from graphics import *
import math
def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc

def to_numbers(strnums):
    for i in range(len(strnums)):
        strnums[i] = float(strnums[i])

def write_sum_of_squares():
    in_file_name = input("File name: ")
    out_file_name = input("File name: ")
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")
    for line in in_file:
        nums = line.split()
        to_numbers(nums)
        square_each(nums)
        summation = sum_list(nums)
        out_file.write("Sum of Squares = " + str(summation))

def starter():
    weight = float(input("Input weight"))
    num_wins = eval(input("Input number of wins"))
    isstarter = False
    if weight >= 150 and weight < 160 and num_wins > 5:
        isstarter = True
    elif weight > 199: isstarter = True
    elif num_wins > 20: isstarter = True

    if isstarter:
        print("He's a starter!")
    else: print("B-Team!")

def leap_year():
    # year%4 and year%400 and year%100
    year = eval(input("What year?"))
    leap = False
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        leap = True
    return leap
    # if leap:
    #     print(str(year) + " is a leap year")
    # else:
    #     print(str(year) + " is not a leap year")



def circleoverlap():
    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2. getY()) ** 2)
    c1 = Circle(p1, r)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    dist = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)

    text_pt = Point(200, 300)
    if dist <= r + r2:
        overlaptext = Text(text_pt, "The circles overlap")
    else:
        overlaptext = Text(text_pt, "The circles do not overlap")
    overlaptext.draw(win)

    win.getMouse()
    win.close()

def main():
    # add_ten([5, 2, -3])
    # square_each([3, 5.7, 2])
    # starter()
    # leap_year()
    # circleoverlap()
    write_sum_of_squares()

if __name__ == '__main__':
    main()