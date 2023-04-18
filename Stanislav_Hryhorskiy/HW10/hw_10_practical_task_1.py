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
        area = self.width*self.height
        return f"The area of the {self.TYPE} with sides " \
               f"{self.width} and {self.height} linear units " \
               f"is equal: S = {area} square units."


if __name__ == "__main__":
    side_1 = float(input("Enter the width of the rectangle: "))
    side_2 = float(input("Enter the width of the rectangle: "))
    rect_1 = Rectangle(side_1, side_2)
    print(rect_1.__str__())
    print(rect_1.get_area())
