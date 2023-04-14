number = input("Enter four digit number: ")
print(f'The product of numbers is: {int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])}')
print("Number in reverse order:", str(number)[::-1])
print("Sorted list:", sorted(str(number)))