# First assignment
def get_sum(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

number = int(input("input your number:" ))

print("Sum of digits of yor number is", get_sum(number))

# Second assignment

print("Reverse of digits is", ''.join(list(reversed(str(number)))))

# Third assignment

print("Order from lower to upper digit is ", ''.join(sorted(str(number))))