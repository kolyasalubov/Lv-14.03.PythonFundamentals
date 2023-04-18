# *** Practical task 1 ***
# Create a polygon class and a rectangle class
# that inherits from the polygon class and finds
# the square of rectangle.

class Polygon:
    TYPE = "polygon"

    def __init__(self, sides_number):
        self.sides_number = sides_number

    def __str__(self):
        return f"This is class of a {self.TYPE}. Number of sides is {self.sides_number}."


class Rectangle(Polygon):
    TYPE = "rectangle"

    def __init__(self, width, height):
        super().__init__(sides_number=4)
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return f"The area of the {self.TYPE} with sides " \
               f"{self.width} and {self.height} linear units " \
               f"is equal: S = {area} square units."


class Triangle(Polygon):
    TYPE = "triangle"

    def __init__(self, side_1, side_2, side_3):
        super().__init__(sides_number=3)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    @staticmethod
    def does_triangle_exist(x, y, z):
        condition = (x + y <= z or x + z <= y or y + z <= x)
        return condition

    def get_area(self):
        a, b, c = self.side_1, self.side_2, self.side_3
        if self.__class__.does_triangle_exist(a, b, c):
            return f"A triangle with such sides does not exist!"
        else:
            p = 0.5 * (a + b + c)
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            return f"The area of the {self.TYPE} with sides " \
                   f"{a, b, c} linear units " \
                   f"is equal: S = {area} square units."


if __name__ == "__main__":
    side_w = float(input("Enter the width of the rectangle: "))
    side_h = float(input("Enter the height of the rectangle: "))
    rect_1 = Rectangle(side_w, side_h)
    print(rect_1.__str__())
    print(rect_1.get_area())
    print()

    side_a = float(input("Enter the first side of the triangle: "))
    side_b = float(input("Enter the second side of the triangle: "))
    side_c = float(input("Enter the third side of the triangle: "))
    triangle_1 = Triangle(side_a, side_b, side_c)
    print(triangle_1.__str__())
    print(triangle_1.get_area())
