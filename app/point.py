class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(" + str(self.x) + "," + str(self.y) + ")"

    def isInside(self, boundary):
        return self.x >= boundary.x1 and self.x <= boundary.x2 and self.y >= boundary.y1 and self.y <= boundary.y2
 