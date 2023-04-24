num = input("Input your number: ")
product = 1
for i in num:
    product *= int(i) 
print(product, num[::-1], sorted(num))