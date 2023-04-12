"""
*** Practical task 2 ***
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
print('The sum of numbers: A + B =', num_a + num_b)
print('The difference of two numbers: A - B =', num_a - num_b)
print('The product of numbers: A * B =', num_a * num_b)
print('Division of numbers: A / B =', num_a / num_b)
print('Exponentiation of numbers: A ** B =', num_a ** num_b)
print('Integer division of numbers: A // B =', num_a // num_b)
print('Remainder from division of numbers: A % B =', num_a % num_b)
