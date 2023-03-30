n = int(input('Enter a number to calculate factorial:'))
f = 1
for i in range(n-1):
     f = f*(f + 1)

print(f)    
