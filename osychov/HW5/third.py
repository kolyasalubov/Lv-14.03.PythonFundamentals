# def Factorial(n):
#     f=1
#     while(n>0):
#         f=f*n
#         n=n-1
#     print("Factorial of the number is: ")
#     print(f)

# Factorial(5)


input_number = int(input("Input natural number: "))

fact = 1

if input_number == 1 or input_number == 0:
    print("Factorial {}! =".format(input_number), fact)
    
elif input_number < 0:
    print("Factorial non positive number don't exist")
else:
    for item in range(1,input_number + 1):
        fact *= item
print("Factorial {}! =".format(input_number), fact)
    


