"""
Name: Tyler McCormack
bumper.py

Problem: Homework 8

Certificate of Authenticity:
I certify that this is my original work.
"""
import math
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb


def get_random_color():
    color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color

def get_random(move_amount):
    rand = randint(-move_amount, move_amount)
    return rand

def did_collide(ball, ball2):
    collison = False
    cent1 = ball.getCenter()
    cent2 = ball2.getCenter()
    dist = math.sqrt((cent1.getX() - cent2.getX()) ** 2 + (cent1.getY() - cent2.getY()) ** 2)
    if dist < (2 * ball.getRadius()):
        collison = True
    return collison

def hit_vertical(ball, win):
    hit = False
    cent = ball.getCenter()
    if ((cent.getX() - ball.getRadius()) <= 0) \
            or ((cent.getX() + ball.getRadius()) >= win.getWidth()):
        hit = True
    return hit

def hit_horizontal(ball, win):
    hit = False
    cent = ball.getCenter()
    if ((cent.getY() - ball.getRadius()) <= 0) \
            or ((cent.getY() + ball.getRadius()) >= win.getHeight()):
        hit = True
    return hit

def main():
    win = GraphWin("Bumper Cars", 600, 600)
    acc = 0

    color1 = get_random_color()
    ball1x = 200
    ball1y = 300
    ball1 = Circle(Point(ball1x, ball1y), 50)
    ball1.setFill(color1)
    ball1.draw(win)
    movex1 = get_random(3)
    movey1 = get_random(3)

    color2 = get_random_color()
    ball2x = 400
    ball2y = 300
    ball2 = Circle(Point(ball2x, ball2y), 50)
    ball2.setFill(color2)
    ball2.draw(win)
    movex2 = get_random(3)
    movey2 = get_random(3)

    while acc < 20000:
        acc += 1
        ball1.move(movex1, movey1)
        ball2.move(movex2, movey2)

        if hit_vertical(ball1, win):
            movex1 = movex1 * -1
            # if movex1 > 0:
            #     movex1 = -1 * movex1
            # else:
            #     movex1 = randint(1,3)

        if hit_horizontal(ball1, win):
            movey1 = -1 * movey1
            # if movey1 > 0:
            #     movey1 = -1 * movey1
            # else:
            #     movey1 = randint(1, 3)

        if hit_vertical(ball2, win):
            movex2 = -1 * movex2
            # if movex2 > 0:
            #     movex2 = -1 * movex2
            # else:
            #     movex2 = randint(1,3)

        if hit_horizontal(ball2, win):
            movey2 = -1 * movey2
            # if movey2 > 0:
            #     movey2 = -1 * movey2
            # else:
            #     movey2 = randint(1, 3)

        if did_collide(ball1, ball2):
            movex1 = movex1 * -1
            movey1 = movey1 * -1
            movex2 = movex2 * -1
            movey2 = movey2 * -1
    win.getMouse()


if __name__ == '__main__':
    main()
