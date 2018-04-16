from rectangle import Rectangle
from graphics import Rectangle as gRectangle
from graphics import Point as gPoint

class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.isDivided = False
        self.points = []
        self.northwest = None
        self.northeast = None
        self.southwest = None
        self.southeast = None

    def __str__( self ):
        return "QuadTree("+ self.boundary.__str__()

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
        self.southeast = QuadTree(Rectangle(mx, my, x2, y2), self.capacity)

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

    def query(self, boundary):
        result = []

        if(not self.boundary.doOverlap(boundary)):
            return result

        if(not self.northwest is None):
            result.extend(self.northwest.query(boundary))

        if(not self.northeast is None):
            result.extend(self.northeast.query(boundary))

        if(not self.southwest is None):
            result.extend(self.southwest.query(boundary))

        if(not self.southeast is None):
            result.extend(self.southeast.query(boundary))

        for i in self.points:
            if i.isInside(boundary):
                result.append(i)

        return result
