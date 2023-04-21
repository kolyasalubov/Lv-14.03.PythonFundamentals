class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides = 4)
        self.width = width
        self.height = height

    def square(self):
        if self.width != self.height and self.width > 0 and self.height > 0:
            return f"The square of rectangle: {self.width*self.height}"
        else:
            return """You're trying to find the area of a square,
            even though you're calling it for an object of the Rectangle class"""
        

if __name__ == "__main__":
    width = int(input("Enter the width of rectangle: "))
    height = int(input("Enter the height of rectangle: "))
    rectangle = Rectangle(width, height)
    print(rectangle.square())
