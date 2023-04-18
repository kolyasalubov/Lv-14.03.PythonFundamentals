even_numbers = []
odd_numbers = []
numbers_not_divisible_by_2_and_3 = []

for number in range(1,10):
    if number % 2 == 0:
       even_numbers.append(number)
    elif number % 3 == 0:
        odd_numbers.append(number)
    else: numbers_not_divisible_by_2_and_3.append(number)

print(even_numbers)
print(odd_numbers)
print(numbers_not_divisible_by_2_and_3)



