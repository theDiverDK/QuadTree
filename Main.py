from graphics import GraphWin

from quadtree import QuadTree
from point import Point
from rectangle import Rectangle


def main():
    test3 = Rectangle(20, 30, 40, 50)
    test4 = QuadTree(test3, 10)
  
  
    print(test3.Print())
    print(test4.Print())
    win = GraphWin('Face', 800, 600)  # give title and dimensions

    win.getMouse()
    win.close()


main()
