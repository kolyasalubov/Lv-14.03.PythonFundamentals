n = int(input("Write the number of digits you want to show:"))

f = [0, 1]
numbers = 2
for digit in f:
    if numbers == n:
        break
    else:
        digit_next = f[-1] + f[-2]
    f.append(digit_next)
    numbers = numbers + 1

print(f)
