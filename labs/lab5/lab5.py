"""
Name: Tyler McCormack
lab5.py

Certificate or Authenticity: I certify that this is my original work.
"""

from graphics import *
from math import sqrt

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    tri = Polygon(p1, p2, p3)
    dxline1 = p1.getX() - p2.getX()
    dyline1 = p1.getY() - p2.getY()
    dxline2 = p2.getX() - p3.getX()
    dyline2 = p2.getY() - p3.getY()
    dxline3 = p3.getX() - p1.getX()
    dyline3 = p3.getY() - p1.getY()
    side1 = sqrt(dxline1 ** 2 + dyline1 ** 2)
    side2 = sqrt(dxline2 ** 2 + dyline2 ** 2)
    side3 = sqrt(dxline3 ** 2 + dyline3 ** 2)
    perimeter = side1 + side2 + side3
    s = perimeter / 2
    area = sqrt(s * (s - side1) * (s - side2) * (s - side1))
    tri.draw(win)
    tex = Text(Point(250, 430), "The perimeter is " + str(perimeter) + " and the area is " + str(area))
    tex.draw(win)
    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions color_rgb funct
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text_input = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text_input = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text_input = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_text_input.draw(win)
    green_text_input.draw(win)
    blue_text_input.draw(win)
    win.getMouse()
    shadeR = eval(red_text_input.getText())
    shadeG = eval(green_text_input.getText())
    shadeB = eval(blue_text_input.getText())
    circlecolor = color_rgb(shadeR, shadeG, shadeB)
    shape.setFill(circlecolor)
    win.getMouse()
    shadeR = eval(red_text_input.getText())
    shadeG = eval(green_text_input.getText())
    shadeB = eval(blue_text_input.getText())
    circlecolor = color_rgb(shadeR, shadeG, shadeB)
    shape.setFill(circlecolor)
    win.getMouse()
    shadeR = eval(red_text_input.getText())
    shadeG = eval(green_text_input.getText())
    shadeB = eval(blue_text_input.getText())
    circlecolor = color_rgb(shadeR, shadeG, shadeB)
    shape.setFill(circlecolor)
    win.getMouse()
    shadeR = eval(red_text_input.getText())
    shadeG = eval(green_text_input.getText())
    shadeB = eval(blue_text_input.getText())
    circlecolor = color_rgb(shadeR, shadeG, shadeB)
    shape.setFill(circlecolor)
    win.getMouse()
    shadeR = eval(red_text_input.getText())
    shadeG = eval(green_text_input.getText())
    shadeB = eval(blue_text_input.getText())
    circlecolor = color_rgb(shadeR, shadeG, shadeB)
    shape.setFill(circlecolor)
    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    stringchars = input("Enter a string of characters")
    print("First character is: ", stringchars[0])
    print("Last character is:", stringchars[-1])
    print("Characters 2-5", stringchars[2:6])
    firstlast = stringchars[0] + stringchars[-1]
    print("Concatenation of first and last: ", firstlast)
    print("First three characters ten times: ")
    firstthree = stringchars[0:3]
    for i in range(10):
        print(firstthree)
    print("Vertical version: ")
    for c in range((len(stringchars))):
        print(stringchars[c])
    print("Length of string: ", len(stringchars))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[1], values[2], values[3]]
    print(x)
    x = [values[1], values[2], values[0]]
    print(x)
    x = [values[2], values[0], float(values[-1])]
    print(x)
    x = values[0] + values[2] + float(values[-1])
    print(x)
    x = len(values)
    print(x)

def another_series():
    numTerms = eval(input("How many terms would you like to sum? "))
    acc = 0
    for i in range(numTerms):
        term = 2 +(2 * (i % 3))
        print(term, end=" ")
        acc = acc + term
    print()
    print("sum = ", acc)


def main():
    # target()
     triangle()
     color_shape()
     process_string()
     process_list()
     another_series()
    #pass


if __name__ == '__main__':
    main()
