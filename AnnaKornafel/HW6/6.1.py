# Even numbers divisible by 2
divisible_2 = [num for num in range(1, 11) if num % 2 == 0]

# Odd numbers divisible by 3
divisible_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 == 0]

# Numbers not divisible by 2 and 3
not_divisible = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]

print("Even numbers divisible by 2:", divisible_2)
print("Odd numbers divisible by 3:", divisible_3)
print("Numbers not divisible by 2 and 3:", not_divisible)