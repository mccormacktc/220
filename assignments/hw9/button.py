"""
Name: Tyler McCormack
button.py
Certificate of Authenticity:
I certify that this is my original work.
"""
from graphics import Text

class Button:
    def __init__(self, shape, label):
        self.shape = shape
        text_pt = self.shape.getCenter()
        buttonlabel = Text(text_pt, label)
        self.label = buttonlabel

    def get_label(self):
        return self.label

    def draw(self, win):
        self.shape.draw(win)
        self.label.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.label.undraw()

    def is_clicked(self, pt):
        center = self.shape.getCenter()
        x1 = center.getX() - 50
        x2 = center.getX() + 50
        y1 = center.getY() - 50
        y2 = center.getY() + 50
        if x2 > pt.getX() > x1 and y2 > pt.getY() > y1:
            return True

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        text_pt = self.shape.getCenter()
        buttonlabel = Text(text_pt, label)
        self.label = buttonlabel
