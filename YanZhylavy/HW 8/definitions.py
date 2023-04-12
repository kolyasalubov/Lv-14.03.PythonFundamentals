import math
def rectangle_area(lenght,width):
  """
  Function calculates area of a rectangle
  using the lenght and width entered by the user 
  """  
  return lenght*width

def triangle_area(base,height):
  """
  Function calculates area of a triangle
  using the base and height entered by the user
  """   
  return 0.5*base*height

def circle_area(radius):
  """
  Function calculates area of a circle
  using the radius entered by the user 
  """
  return math.pi*math.pow(radius,2)