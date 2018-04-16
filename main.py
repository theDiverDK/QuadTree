import random
from quadtree import QuadTree
from point import Point
from rectangle import Rectangle
from graphics import Rectangle as gRectangle, Point as gPoint, GraphWin


def main():
    width = 800
    height = 600
    border = 20

    x1, y1, x2, y2 = border, border, width-border, height-border

    rect = Rectangle(x1, y1, x2, y2)
    qt = QuadTree(rect, 4)

    for _ in range(5000):
        qt.insert(Point(random.randrange(x1, x2),
                        random.randrange(y1, y2)))

    print('data ', qt.getLoadAndCapacity())

    win = GraphWin('Quadtree', width, height, autoflush=False)
    print(qt)
    qt.show(win)
    mrect = None
    while True:
        mouse = win.checkMouse()

        if not mouse is None:
            if mouse.x >= border and mouse.x <= width-border and mouse.y >= border and mouse.y <= width-border:
                for item in win.items[:]:
                    item.undraw()

                mrect = gRectangle(
                    gPoint(mouse.x-border, mouse.y-border), gPoint(mouse.x+border, mouse.y+border))
                mrect.draw(win)

                boundary = Rectangle(
                    mrect.p1.getX(), mrect.p1.getY(), mrect.p2.getX(), mrect.p2.getY())

                hits = qt.query(boundary)

                #ToDo: optimize to send list instead, because the points are close
                for hit in hits:
                    qt.remove(hit)

                qt.show(win)
                win.update()

    win.close()


main()
