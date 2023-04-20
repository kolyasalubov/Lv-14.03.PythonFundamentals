class Polygon:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


class Rectangle(Polygon):
    def __init__(self, width, length):
        Polygon.__init__(self, 4)
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
def main():
    rect = Rectangle(2,3) 
    print(rect.area()) 
main()