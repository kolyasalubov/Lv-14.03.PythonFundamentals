class Polygon():
    def __init__(self, num_of_sides):
        self.num = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def Inputting(self):
        self.sides = [float(input(f"Enter your {i+1}side: ")) for i in range(self.num)]
        print(self.sides)


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def rectangleArea(self):
        a, b = self.sides
        area = a * b
        print(area)

r = Rectangle()

r.Inputting()
r.rectangleArea()