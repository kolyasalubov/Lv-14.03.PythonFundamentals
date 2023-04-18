class Polygon:
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides


class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__(4)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


rectangle = Rectangle(2, 3)
area = rectangle.area()
print(area)
