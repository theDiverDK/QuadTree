class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def Print(self):
        return "Rectangle("+str(self.x) + ","+str(self.y)+","+str(self.w)+","+str(self.h)+")"
