def largest_num(num1, num2):
    """
In this code we check if num1 > num2;
if it is, we return 'num1 is largest'
else, we return 'num2 is largest'
    """
    return f"{num1} is largest" if num1 > num2 else f"{num2} is largest"


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(largest_num(num1, num2))