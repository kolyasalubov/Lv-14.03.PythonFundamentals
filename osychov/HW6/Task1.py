even_numbers = [i for i in range(1, 10) if i % 2 == 0 ]
odd_numbers = [i for i in range(1, 10) if i % 3 == 0 ]
not_divisible_2_3 = [i for i in range(1, 10) if i % 3 != 0 and i %2 !=0  ]
print("Even nimbers that are divisible by 2: ", even_numbers)
print("Odd numbers , which are divisible by 3: ", odd_numbers)
print("numbers that are not divisible by 2 and 3: ", not_divisible_2_3)