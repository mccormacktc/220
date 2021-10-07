"""
Name: Tyler McCormack
template.py

Problem: This is a template for all future code

Certificate of Authenticity:
I certify that this is my original work.
"""
from graphics import GraphWin, Circle, Point, Polygon, Text, Line

def drawheart(window):
    heart1 = Circle(Point(226, 201), 25)
    heart2 = Circle(Point(274, 201), 25)
    heart3 = Polygon(Point(205, 215), Point(295, 215), Point(250, 270))
    heart4 = Circle(Point(250, 212), 5)
    heart1.setFill("red")
    heart2.setFill("red")
    heart3.setFill("red")
    heart4.setFill("red")
    heart1.setOutline("red")
    heart2.setOutline("red")
    heart3.setOutline("red")
    heart4.setOutline("red")
    heart1.draw(window)
    heart2.draw(window)
    heart3.draw(window)
    heart4.draw(window)

def main():
    win = GraphWin("Greeting Card", 500, 500)
    # heart1 = Circle(Point(226, 201), 25)
    # heart1.draw(win)
    # heart2 = Circle(Point(274, 201), 25)
    # heart2.draw(win)
    # heart3 = Polygon(Point(205, 215), Point(295, 215), Point(250, 270))
    # heart3.draw(win)
    # heart4 = Circle(Point(250, 212), 5)
    # heart4.draw(win)
    # heart1.setFill("red")
    # heart2.setFill("red")
    # heart3.setFill("red")
    # heart4.setFill("red")
    # heart1.setOutline("red")
    # heart2.setOutline("red")
    # heart3.setOutline("red")
    # heart4.setOutline("red")
    drawheart(win)
    vdaytxt_pt = Point(250, 150)
    vdaytxt = Text(vdaytxt_pt, "Happy Valentine's Day!")
    vdaytxt.draw(win)

    win.getMouse()

    # for x in range(510):
    #     backgroundw = win.getWidth()
    #     backgroundh = win.getHeight()
    #     background = Rectangle(Point(0,0), Point(backgroundw, backgroundh))
    #     background.setOutline("white")
    #     background.setFill("white")
    #     background.draw(win)
    #     drawheart(win)
    bodyp2 = Point(30, 222)
    tipp1 = Point(25, 227)
    tipp2 = Point(25, 217)
    arrowbody = Line(Point(0, 222), bodyp2)
    arrowtip1 = Line(bodyp2, tipp1)
    arrowtip2 = Line(bodyp2, tipp2)
    heart2 = Circle(Point(274, 201), 25)
    heart2.setFill("red")
    heart2.setOutline("red")
    heart3 = Polygon(Point(250, 215), Point(295, 215), Point(250, 270))
    heart3.setFill("red")
    heart3.setOutline("red")
    arrowbody.draw(win)
    arrowtip1.draw(win)
    arrowtip2.draw(win)
    heart2.draw(win)
    heart3.draw(win)
    seam1 = Line(Point(250, 222), Point(249, 220))
    seam2 = Line(Point(250, 222), Point(249, 224))
    for _ in range(100):
        arrowbody.move(5, 0)
        arrowtip1.move(5, 0)
        arrowtip2.move(5, 0)
        if _ == 47:
            seam2.draw(win)
            seam1.draw(win)

    closetxt = Text(Point(250, 400), "Click again to close!")
    closetxt.draw(win)
    win.getMouse()

if __name__ == '__main__':
    main()
