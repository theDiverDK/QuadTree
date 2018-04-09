
class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity

    def Print(self):
        return "QuadTree("+self.boundary.Print() + ","+str(self.capacity)+")"
