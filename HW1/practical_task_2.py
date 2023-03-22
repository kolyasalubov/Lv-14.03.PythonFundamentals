"""
WRITE A PROGRAM THAT WILL CALCULATE THE SUM,
DIFFERENCE, PRODUCT, EXPONENTIATION ETC.
OF TWO NUMBERS A AND B THAT THE PROGRAM READS
FROM THE CONSOLE (DATA ENTERED BY THE USER)
AND WILL OUTPUT APPROPRIATE RESULT:
"A + B = "  ...
"A - B = "   ...
"A * B = "   ...
"A / B = "   ...
"A**B = "   ...
"A//B = "   ...
"A%B = "  ...
"""

num_a = float(input('Input first number A = '))
num_b = float(input('Input second number B = '))

print()
print('A + B =', num_a + num_b)
print('A - B =', num_a - num_b)
print('A * B =', num_a * num_b)
print('A / B =', num_a / num_b)
print('A ** B =', num_a ** num_b)
print('A // B =', num_a // num_b)
print('A % B =', num_a % num_b)
