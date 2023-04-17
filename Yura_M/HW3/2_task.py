number = int(input("Enter 4 number: "))
a = str(number)
dob = 0
for n in a:
    conver = int(n)
    dob += conver
print("suma :", dob)


revers = a[::-1]
print("This number revers: ", revers)

up = sorted(a)
print("sort up: ", up)
