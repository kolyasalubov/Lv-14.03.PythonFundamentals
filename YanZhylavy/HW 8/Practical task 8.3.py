import definitions as defi
greetings = int(input('''Hello! With this programm you can
calculate area of rectangle, triangle or circle. Please, enter 1 for rectangle, 2 for triangle and 3 for circle: '''))
if greetings == 1:
    lenght = input('Enter lenght: ')
    wid = input('Enter widght: ')
    print('The answer is: ', round(defi.rectanle_area(float(len),float(wid)),2))

elif greetings == 2:
    base = input('Enter base:')
    height = input('Enter height: ')
    print("The answer is: ", round(defi.triangle_area(float(base),float(height)),2))

elif greetings == 3:
     radius = input('Enter radius: ')
     print('The answer is: ', round(defi.circle_area(float(radius)),2))
else:
    print('''Error. Make sure that you have entered 
the correct data.''')