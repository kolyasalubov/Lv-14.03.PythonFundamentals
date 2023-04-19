


def area_rectangle():
    length = int(input('Enter a length: '))
    breadth = int(input('Enter a breath: '))
    area = length * breadth 
    return f'The area of rectangle = {area} cm2.'
#print(area_rectangle())


def area_triangle():
    base = int(input('Enter a base : '))
    height = int(input('Enter a height : '))
    area = 0.5 * (base*height)
    return f'The area of triangle = {area} cm2.'
#print(area_triangle())



def area_circle():
    radius = int(input('Enter a radius : '))    
    import math
    area = math.pi * radius**2
    return f'The area of circle = {area:.2f} cm2.'
#print(area_circle())



def calc_area():
    option = input('Choose option:\n1.Rectangle\n2.Triangle\n3.Cirlce\n').lower()
    if option == 'Rectangle' or option == '1':
        return (area_rectangle())
    elif option == 'Triangle' or option =='2':
        return (area_triangle())
    elif option == 'Circle' or option == '3':
        return (area_circle())
    else:
        return 'Invalid option.'
print(calc_area())


#Спробую з import в домашці у 8 темі).