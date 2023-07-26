class Polygon:
    def __init__(self, num_of_sides):
       if num_of_sides>3:
            print('Sorry,we haven`t studied so complicated shapes yet')
       self.n = num_of_sides
       self.sides = [0 for i in range(num_of_sides)]
    def input_sides(self):
      self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
      if len(self.sides) == 3:
          a, b, c = self.sides
          if not a+b>c and a+c>b and b+c>a:
              print('Triangle is impossible')   
    def disp_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

  

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
       
    def triangle_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return f'The area of the triangle is {round(area,2)}'  
    
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)    #There was an issue. Rectangle need only 2 sides to be defined.
                               #Otherwise, if you define 4 sides with different values, you will get
    def rectangle_area(self):  #an irregular quadrilateral, which is not included in the conditions of the task
        a,b, = self.sides
        return a*b                            
                               