"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)


    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        userClick = win.getMouse()
        # builds a circle
        shape = Rectangle(Point(userClick.x - 10, userClick.y - 10), Point(userClick.x + 10, userClick.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

        # move amount is distance from center of circle to the
        # # point where the user clicked
        # dx = p.getX() - c.getX()
        # dy = p.getY() - c.getY()
        # shape.move(dx, dy)

    final_pt = Point(width / 2, 20)
    final = Text(final_pt, "Click to close the window")
    final.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Rectangles Function", 400, 400)
    point1 = win.getMouse()
    point2 = win.getMouse()
    rect = Rectangle(point1, point2)
    rect.draw(win)

    shapeWidth = abs(point1.getX() - point2.getX())
    shapeLength = abs(point1.getY() - point2.getY())

    area = shapeLength * shapeWidth

    area_pt = Point(200, 200)
    areatxt = Text(area_pt, "The area is: " + str(area))
    areatxt.draw(win)

    per_pt = Point(200, 300)
    perimeter = 2 * (shapeWidth + shapeLength)
    pertxt = Text(per_pt, "The perimeter is: " + str(perimeter))
    pertxt.draw(win)

    win.getMouse()
    win.close()

def circle():
    win = GraphWin("Circle Function", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    r = math.sqrt((x2 - x1) ** 2 + (y2-y1) ** 2)
    circ = Circle(p1, r)
    circ.draw(win)

    rad_pt = Point(200, 20)
    radtxt = Text(rad_pt, "The radius is " + str(r) + ". Please click again to close the window")
    radtxt.draw(win)

    win.getMouse()
    win.close()



def pi2():
    numPi = eval(input("Enter the number of terms for approximation of pi: "))
    acc = 0
    for i in range(numPi):
        num = 4
        denom = 1 + 2 * i
        frac = (num / denom) * ((-1)**i)
        acc = acc + frac
    print(acc)
    print(math.pi - acc)

def main():
    # squares()
    # rectangle()
    # circle()
    # pi2()


main()
