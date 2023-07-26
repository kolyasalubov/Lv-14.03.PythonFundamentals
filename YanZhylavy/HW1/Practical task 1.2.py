name = input("Enter your name, please: ")

print(f"Hello, {name}. I`d like to show you results of different math calculations on some numbers entered by you. Let it be 'a' and 'b' \U0001f600 ")

a = int(input("your 'a' is: "))
b = int(input("your 'b' is: "))

print("The results:\nAddition is:", a + b,"\nSubtraction is:", a-b,
      "\nMultiplication is:", a*b,"\nDivision is:", a/b,"\nFloor division is:",
      a//b,"\nExponentiation is:",a**b,"\nModulus is:",a%b)
