"""
*** Practical task 2 ***
Print Fibonacci numbers up to the entered number n, using cycles.
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
"""

number = int(input("Enter the number of Fibonacci sequence to be displayed: "))

num_prev, num_next = 0, 1
print(f"The first numbers of the Fibonacci sequence in quantity n = {number}:", end=' ')

for element in range(number):
    print(num_prev, end='; ' if element != number - 1 else '.')
    num_prev, num_next = num_next, num_prev + num_next

# The Binet formula for Fibonacci sequence
print(f"\nThe first numbers of the Fibonacci sequence in quantity n = {number}:", end=' ')
fi, psi = 0.5 * (1 + 5 ** 0.5), 0.5 * (1 - 5 ** 0.5)
for item in range(number):
    fibo_num = round((fi ** item - psi ** item) / (fi - psi))
    print(fibo_num, end='; ' if item != number - 1 else '.')

# Example of program operation
# Enter the number of Fibonacci sequence to be displayed: 8
# The first numbers of the Fibonacci sequence in quantity n = 8: 0; 1; 1; 2; 3; 5; 8; 13.
# Process finished with exit code 0
