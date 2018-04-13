from rectangle import Rectangle
from graphics import Rectangle as gRectangle
from graphics import Point as gPoint


class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.isDivided = False
        self.points = []

    def print(self):
        return "QuadTree("+self.boundary.print()

    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True

        if not self.isDivided:
            self.subDivide()

        if self.northwest.insert(point):
            return True
        elif self.northeast.insert(point):
            return True
        elif self.southwest.insert(point):
            return True
        elif self.southeast.insert(point):
            return True

    def subDivide(self):
        x1, y1, x2, y2 = self.boundary.x1, self.boundary.y1, self.boundary.x2, self.boundary.y2

        mx = int((x1 + x2) / 2)
        my = int((y1 + y2) / 2)

        self.northwest = QuadTree(Rectangle(x1, y1, mx, my), self.capacity)
        self.northeast = QuadTree(Rectangle(mx, y1, x2, my), self.capacity)
        self.southwest = QuadTree(Rectangle(x1, my, mx, y2), self.capacity)
        self.southeast = QuadTree(Rectangle(mx, my, mx, y2), self.capacity)

        self.isDivided = True

    def show(self, win):
        x1, y1, x2, y2 = self.boundary.x1, self.boundary.y1, self.boundary.x2, self.boundary.y2

        for point in self.points:
            p = gPoint(point.x, point.y)
            p.draw(win)

        rect = gRectangle(gPoint(x1, y1), gPoint(x2, y2))
        rect.draw(win)

        if self.isDivided:
            self.northwest.show(win)
            self.northeast.show(win)
            self.southwest.show(win)
            self.southeast.show(win)
