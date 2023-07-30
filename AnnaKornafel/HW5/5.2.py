def fibonacci(n):
    fibonacci_list = [0, 1]
    a, b = 0, 1


    while b <= n:
        a, b = b, a + b
        if b <= n:
            fibonacci_list.append(b)

    return fibonacci_list

try:
    n = int(input("Enter a number: "))
    if n < 0:
        print("Print positive number.")
    else:
        fibonacci_seq = fibonacci(n)
        print("Fibonacci nambers to ", n, "are ", fibonacci_seq)  
except ValueError:
    print("Invalid input.")          

