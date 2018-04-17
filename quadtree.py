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

    def __str__(self):
        return "QuadTree(" + self.boundary.__str__()

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

        if not self.boundary.doOverlap(boundary):
            return result

        if self.isDivided:
            result.extend(self.northwest.query(boundary))
            result.extend(self.northeast.query(boundary))
            result.extend(self.southwest.query(boundary))
            result.extend(self.southeast.query(boundary))

        for i in self.points:
            if i.isInside(boundary):
                result.append(i)

        return result

    def getLoadAndCapacity(self):
        load = 0
        totalCapacity = 0
        load += len(self.points)
        totalCapacity += self.capacity

        if self.isDivided:
            tempLoad, tempTotalCapacity = self.northwest.getLoadAndCapacity()
            load += tempLoad
            totalCapacity += tempTotalCapacity
            tempLoad, tempTotalCapacity = self.northeast.getLoadAndCapacity()
            load += tempLoad
            totalCapacity += tempTotalCapacity
            tempLoad, tempTotalCapacity = self.southwest.getLoadAndCapacity()
            load += tempLoad
            totalCapacity += tempTotalCapacity
            tempLoad, tempTotalCapacity = self.southeast.getLoadAndCapacity()
            load += tempLoad
            totalCapacity += tempTotalCapacity

        return load, totalCapacity

    def remove(self, point):
        if point in self.points:
            self.points.remove(point)
        elif self.isDivided:
            if point.isInside(self.northwest.boundary):
                self.northwest.remove(point)
            if point.isInside(self.northeast.boundary):
                self.northeast.remove(point)
            if point.isInside(self.southwest.boundary):
                self.southwest.remove(point)
            if point.isInside(self.southeast.boundary):
                self.southeast.remove(point)

            if len(self.northwest.points) == 0 and len(self.northeast.points) == 0 and len(self.southwest.points) == 0 and len(self.southeast.points) == 0:
                self.northwest = None
                self.northeast = None
                self.southwest = None
                self.southeast = None
                self.isDivided = False

        return
