from rectangle import Rectangle
from graphics import Rectangle as gRectangle
from graphics import Point as gPoint


class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.isDivided = False
        self.points = []
        print(boundary.print(), capacity, self.isDivided)

    def print(self):
        return "QuadTree("+self.boundary.print() + ","+str(self.capacity)+")"

    def insert(self, point):
        print(point.x, point.y)
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            print('Inserted:', point.x, point.y)
            return True

        if not self.isDivided:
            self.subDivide()
            print('divided')

        print(self.northwest.insert(point))
        # if self.northwest.insert(point):
        #     print('nw')
        #     return True
        # elif self.northeast.insert(point):
        #     print('ne')
        #     return True
        # elif self.southwest.insert(point):
        #     print('sw')
        #     return True
        # elif self.southeast.insert(point):
        #     print('se')
        #     return True

    def subDivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        mx = int(x + w / 2)
        my = int(y + h / 2)

        self.northwest = QuadTree(Rectangle(x, y, mx, my), self.capacity)
        self.northeast = QuadTree(Rectangle(x+mx, y, x + w, my), self.capacity)
        self.southwest = QuadTree(Rectangle(x, y+my, mx, y + h), self.capacity)
        self.southeast = QuadTree(Rectangle(x+mx, y+my, x + w, y + h), self.capacity)

        print('Divide', self.northwest.print(), self.northeast.print(),
              self.southwest.print(), self.southeast.print())
        self.isDivided = True

    def show(self, win):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        for point in self.points:
            p = gPoint(point.x, point.y)
            p.draw(win)

        print(x, y, w, h, win)
        rect = gRectangle(gPoint(x, y), gPoint(x + w, y + h))
        rect.draw(win)

        if self.isDivided:
            self.northwest.show(win)
            self.northeast.show(win)
            self.southwest.show(win)
            self.southeast.show(win)
