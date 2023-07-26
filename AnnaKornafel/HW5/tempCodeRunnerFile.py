def fibonacci_up_to_n(n):
#     fibonacci_list = [0, 1]
#     a, b = 0, 1

#     while b <= n:
#         a, b = b, a + b
#         if b <= n:
#             fibonacci_list.append(b)

#     return fibonacci_list

# # Get the input from the user
# try:
#     n = int(input("Enter a number to generate Fibonacci sequence up to that number: "))
#     if n < 0:
#         print("Please enter a non-negative integer.")
#     else:
#         fibonacci_sequence = fibonacci_up_to_n(n)
#         print("Fibonacci numbers up to", n, "are:", fibonacci_sequence)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")