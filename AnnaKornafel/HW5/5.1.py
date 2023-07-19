lst = []

try:
    num = int(input("Enter number of list items: "))
    for i in range(1, num):
        lst.append(float(input(f"Enter {i}th item: ")))
    print(lst)
except:
    print("Enter number, not a string! ")