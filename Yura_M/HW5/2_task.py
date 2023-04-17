# # Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

n = int(input("Enter number of values: "))

n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(n1)
else:
    print("fibonacci se uence: ")
    while count < n:
        print(n1, end=', ')
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
