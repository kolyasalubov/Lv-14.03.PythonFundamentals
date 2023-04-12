
n = int(input("Enter a number: "))

f_massive = [0, 1]

while f_massive[-1] < n:
    next_num = f_massive[-1] + f_massive[-2]
    f_massive.append(next_num)

if f_massive[-1] > n:

    f_massive.pop()

print(f_massive)