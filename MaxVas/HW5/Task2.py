n = int(input("Enter your number: "))
lst = [0, 1]

for i in range(2, n):
    lst.append(lst[i-1] + lst[i-2])
print(lst)