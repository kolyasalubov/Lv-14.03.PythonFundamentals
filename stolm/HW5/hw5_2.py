number = int(input("Enter element for searching Fibonacci: "))

first = count = 0
second = 1

if number <= 0:
    print("Error! We can't find it!")
elif number == 1:
    print(f"Fibonacci numbers for {number}: {first}")
else:
    print(f"Fibonacci numbers for {number}: ")
    while count != number:
        print(first)
        sum = first+second
        first = second
        second = sum
        count +=1
