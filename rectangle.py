from point import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def contains(self, point):
        return point.x >= self.x1 and point.y >= self.y1 and point.x < self.x2 and point.y < self.y2

    def print(self):
        return "Rectangle("+str(self.x1) + ","+str(self.y1)+","+str(self.x2)+","+str(self.y2)+")"
