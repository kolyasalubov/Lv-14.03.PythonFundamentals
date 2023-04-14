even_numbers = []
odd_numbers = []
another_numbers = []

for number in range(1, 11):
    if number%2 == 0:
        even_numbers.append(number)
    elif number not in even_numbers and number%3 == 0:
        odd_numbers.append(number)
    else:
        another_numbers.append(number)


print(f'Even numbers: {even_numbers}, odd numbers: {odd_numbers}, another numbers: {another_numbers}')
