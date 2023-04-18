int1 = range(1, 11)
even_numbers = []
odd_numbers = []
none_divisible_numbers = []
for item in list(int1):
    if int(item / 2) == item / 2:
        even_numbers.append(item)
    elif int(item / 3) == item / 3:
        odd_numbers.append(item)
    else:
        none_divisible_numbers.append(item)

print(f"""1) even numbers that are divisible by 2: {even_numbers};\n
2) odd numbers that are divisible by 3: {odd_numbers};\n        
3) numbers that aren't divisible by 2 and 3:{none_divisible_numbers}.""")
