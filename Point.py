class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Print(self):
        return "Point("+str(self.x) + ","+str(self.y)+")"
