n = int(input("Enter your stop number: "))
i = 0
s = 1
print("Sequence of Fibonacci numbers: ", end=" ")
while i <= n:
    print(i, end=' ')
    i, s = s, i+s