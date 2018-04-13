from graphics import GraphWin

import random

from quadtree import QuadTree
from point import Point
from rectangle import Rectangle


def main():
    width = 800
    height = 600
    border = 20
    x1, y1, x2, y2 = border, border, width-border, height-border

    rect = Rectangle(x1, y1, x2, y2)
    qt = QuadTree(rect, 4)

    for _ in range(50):
        qt.insert(Point(random.randrange(x1, x2),
                        random.randrange(y1, y2)))

    win = GraphWin('Quadtree', width, height)  # give title and dimensions

    qt.show(win)

    win.getMouse()
    win.close()


main()
