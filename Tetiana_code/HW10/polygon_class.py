class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0] * num_sides
        
    def input_sides(self):
        self.sides = [float(input("Enter side "+ str(i+1) + ": ")) for i in range(self.num_sides)]
        
    def display_sides(self):
        for i in range(self.num_sides):
            print("Side", i+1, "is", self.sides[i])
            
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
        
    def find_area(self):
        a, b = self.sides
        area = a * b
        print("The area of the rectangle is", area)

