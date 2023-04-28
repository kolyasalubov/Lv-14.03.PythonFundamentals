import calc_area
while True:
    choice = input('What figure area you wanna count?\n1.Rectangle\n2.Triangle\n3.Circle\n4.Close program\nEnter: ')
    if choice == '1':
        num1 = int(input('Enter 1st number: '))
        num2 = int(input('Enter 2nd number: '))
        print(calc_area.rect(num1,num2))
    elif choice == '2':
        num1 = int(input('Enter 1st number: '))
        num2 = int(input('Enter 2nd number: '))
        print(calc_area.tria(num1,num2))
    elif choice == '3':
        num1 = int(input('Enter 1st number: '))
        print(calc_area.circ(num1))
    elif choice == '4':
        break
    else:
        print('Invlaid option!')