class Polygon:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        

class Rectangle(Polygon):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
    def area(self):
        r_area = self.x * self.y
        return f'The area of rectangle is {r_area} cm2.'


num = Rectangle(5,6)
print(num.area())