from graphics import Rectangle, GraphWin, Point

from QuadTree import QuadTree


def main():
    win = GraphWin('Face', 800, 600) # give title and dimensions

    head = Rectangle(Point(100,100),Point(200,200))
    head.draw(win)

    win.getMouse()
    win.close()

main()