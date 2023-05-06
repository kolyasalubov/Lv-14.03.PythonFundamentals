class Polygon():
    def __init__(self, sides):
        self.sides = sides
    def sides_count(self):
        return self.sides


class Rectangle(Polygon):
    def __init__(self, a: int, b: int, sides=4):
        self.a = a
        self.b = b
        self.sides = sides
    def square(self):
        return self.a*self.b
    
