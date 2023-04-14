def rectanle_area(len:float, wid:float)->float:
  """
  Function calculates area of a rectangle
  using the lenght and width entered by the user 
  """  
  return len*wid

def triangle_area(base:float, height:float)->float:
  """
  Function calculates area of a triangle
  using the base and height entered by the user
  """   
  return 0.5*base*height

def circle_area(rad:float)->float:
  """
  Function calculates area of a circle
  using the radius entered by the user 
  """
  PI = 3.14  
  return PI*rad**2
    

greetings = input("""Hello! With this programm you can
calculate area of rectangle, triangle or circle. Please,select
a figure: """)

if greetings == "Triangle" or greetings == "triangle":
    base = input("Enter base:")
    height = input("Enter height:")
    print("The answer is: ", triangle_area(float(base),float(height)))

elif greetings == "Rectangle" or greetings == "rectangle":
    len = input("Enter lenght: ")
    wid = input("Enter widght: ")
    print("The answer is: ", rectanle_area(float(len),float(wid)))

elif greetings == "Circle" or greetings == "circle":
     rad = input("Enter radius: ")
     print("The answer is: ", circle_area(float(rad)))
else:
    print("""Error. Make sure that you have entered 
the correct data""")
