class Polygon:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b


class Rectangle(Polygon):

    def sq_rec(self):
        s = self.a * self.b
        return s 
