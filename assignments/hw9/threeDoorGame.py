"""
Name: Tyler McCormack
template.py

Problem: This is a template for all future code

Certificate of Authenticity:
I certify that this is my original work.
"""
from button import Button
from graphics import GraphWin, Text, Point, Rectangle
from random import randint

def main():
    win = GraphWin("3door", 600, 400)

    secret_door = randint(0, 3)
    headertext = "I have a secret door."
    header_pt = Point(300, 50)
    header = Text(header_pt, headertext)
    header.draw(win)

    footertext = "Click to choose my door!"
    footer_pt = Point(300, 350)
    footer = Text(footer_pt, footertext)
    footer.draw(win)


    but1rec = Rectangle(Point(250, 150), Point(350, 250))
    but1 = Button(but1rec, "Door 2")
    # but1.color_button("red")
    but1.draw(win)


    but2rec = Rectangle(Point(50, 150), Point(150, 250))
    but2 = Button(but2rec, "Door 1")
    but2.draw(win)

    but3rec = Rectangle(Point(450, 150), Point(550, 250))
    but3 = Button(but3rec, "Door 3")
    but3.draw(win)


    guess = win.getMouse()

    if but1.is_clicked(guess):
        if secret_door == 0:
            but1.undraw()
            but1.color_button("green")
            but1.draw(win)
            header.undraw()
            headertext = "You win!"
            header = Text(header_pt, headertext)
            header.draw(win)
            footer.undraw()
            footertext = "Click to close"
            footer = Text(footer_pt, footertext)
            footer.draw(win)
        else:
            but1.undraw()
            but1.color_button("red")
            but1.draw(win)
            header.undraw()
            headertext = "You Lost!"
            header = Text(header_pt, headertext)
            header.draw(win)
            footer.undraw()
            footertext = "Door " + str(secret_door + 1) + " is my secret door"
            footer = Text(footer_pt, footertext)
            footer.draw(win)
    elif but2.is_clicked(guess):
        if secret_door == 1:
            but2.undraw()
            but2.color_button("green")
            but2.draw(win)
            header.undraw()
            headertext = "You win!"
            header = Text(header_pt, headertext)
            header.draw(win)
            footer.undraw()
            footertext = "Click to close"
            footer = Text(footer_pt, footertext)
            footer.draw(win)
        else:
            but2.undraw()
            but2.color_button("red")
            but2.draw(win)
            header.undraw()
            headertext = "You Lost!"
            header = Text(header_pt, headertext)
            header.draw(win)
            footer.undraw()
            footertext = "Door " + str(secret_door + 1) + " is my secret door"
            footer = Text(footer_pt, footertext)
            footer.draw(win)
    elif but3.is_clicked(guess):
        if secret_door == 2:
            but3.undraw()
            but3.color_button("green")
            but3.draw(win)
            header.undraw()
            headertext = "You win!"
            header = Text(header_pt, headertext)
            header.draw(win)
            footer.undraw()
            footertext = "Click to close"
            footer = Text(footer_pt, footertext)
            footer.draw(win)
        else:
            but3.undraw()
            but3.color_button("red")
            but3.draw(win)
            header.undraw()
            headertext = "You Lost!"
            header = Text(header_pt, headertext)
            header.draw(win)
            footer.undraw()
            footertext = "Door " + str(secret_door + 1) + " is my secret door"
            footer = Text(footer_pt, footertext)
            footer.draw(win)

    win.getMouse()

if __name__ == '__main__':
    main()