from point import Point


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return point.x >= self.x and point.y >= self.y and point.x < self.x + self.w and point.y < self.y + self.h

    def print(self):
        return "Rectangle("+str(self.x) + ","+str(self.y)+","+str(self.w)+","+str(self.h)+")"
