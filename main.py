from graphics import GraphWin

import random

from quadtree import QuadTree
from point import Point
from rectangle import Rectangle


def main():
    width = 800
    height = 600
    rect = Rectangle(20, 20, width-40, height-40)
    qt = QuadTree(rect, 4)

#    for _ in range(5):
#        qt.insert(Point(random.randrange(0, width),
#                        random.randrange(0, height)))

    qt.insert(Point(100, 100))
    qt.insert(Point(110, 100))
    qt.insert(Point(120, 100))
    qt.insert(Point(130, 100))
    qt.insert(Point(140, 100))
    win = GraphWin('Quadtree', width, height)  # give title and dimensions

    qt.show(win)

    win.getMouse()
    win.close()


main()
