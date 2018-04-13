from graphics import GraphWin

import random

from quadtree import QuadTree
from point import Point
from rectangle import Rectangle
from graphics import Rectangle as gRectangle, Point as gPoint


def main():
    width = 800
    height = 600
    border = 20

    x1, y1, x2, y2 = border, border, width-border, height-border

    rect = Rectangle(x1, y1, x2, y2)
    qt = QuadTree(rect, 4)

    for _ in range(100):
        qt.insert(Point(random.randrange(x1, x2),
                        random.randrange(y1, y2)))

    win = GraphWin('Quadtree', width, height)

    qt.show(win)
    mrect = None
    while True:
        mouse = win.checkMouse()
        print(mouse)
        if not mouse is None:

            if not mrect is None:
                mrect.undraw(win)
                print("undraw")
            if mouse.x >= border and mouse.x <= width-border and mouse.y >= border and mouse.y <= width-border:
                mrect = gRectangle(gPoint(mouse.x-border, mouse.y-border), gPoint(mouse.x+border, mouse.y+border))
                mrect.draw(win)

    win.close()


main()
