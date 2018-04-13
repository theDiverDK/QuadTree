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

    for _ in range(100):
        qt.insert(Point(random.randrange(x1, x2),
                        random.randrange(y1, y2)))

    win = GraphWin('Quadtree', width, height)

    while True:
        qt.show(win)
        mouse=win.getMouse()
        print(mouse.x,mouse.y)
        qt.insert(Point(mouse.x, mouse.y))

    win.close()


main()
