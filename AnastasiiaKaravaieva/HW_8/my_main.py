import module_of_areas


area = input("What kind of area do you want to find?").lower()

if area == "triangle":
    h_t = int(input("Write the height of triangle:"))
    a_t = int(input("Write the side of triangle:"))
    print(module_of_areas.triangle_area(h_t, a_t))
elif area == "rectangle":
    a_r = int(input("Write the first side of rectangle:"))
    b_r = int(input("Write the second side of rectangle:"))
    print(module_of_areas.rectangle_area(a_r, b_r))
elif area == "circle":
    r_c = int(input("Write the r of the circle:"))
    print(module_of_areas.circle_area(r_c))
else:
    print("I don't know how to find the area of this figure")