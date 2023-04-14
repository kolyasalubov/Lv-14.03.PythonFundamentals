num1 = 0
num2 = 1
 
number = int(input("Write number of digit: "))
if number <=0 :
    print("Please enter a positive integer")
else:
    print(num1, num2, end=' ')
    for i in range(2, number):
        num1, num2 = num2, num1 + num2
        print(num2, end=' ')

 