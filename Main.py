from graphics import GraphWin

import QuadTree
import Point
import Rectangle


def main():
    test3 = Rectangle.Rectangle(20, 30, 40, 50)
    test4 = QuadTree.QuadTree(test3, 10)
  
  
    print(test3.Print())
    print(test4.Print())
    win = GraphWin('Face', 800, 600)  # give title and dimensions

    win.getMouse()
    win.close()


main()
