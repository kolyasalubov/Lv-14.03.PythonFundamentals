import Finding_Area_Module


finding = input("What kind of figure do you need the area for?:").lower()
if finding == "rectangle":
    print("The Area of Rectangle is:", Finding_Area_Module.area_rectangle(
        length=int(input("Enter length of your Rectangle:")),
        width=int(input("Enter width of your Rectangle:"))))
elif finding == "triangle":
    print("The Area of Triangle is:", Finding_Area_Module.area_triangle(
        height=int(input("Enter height of your Triangle:")),
        base=int(input("Enter base of your Triangle:"))))


elif finding == "circle":
    print("The Area of your Circle is:", Finding_Area_Module.area_circle(
        radius=int(input("Enter radius of your Circle:"))))
