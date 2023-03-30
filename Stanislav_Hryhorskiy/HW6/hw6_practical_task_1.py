"""
*** Practical task 1 ***
In the range from 1 to 10 determine:
• even numbers that are divisible by 2;
• odd numbers, which are divisible by 3;
• numbers that are not divisible by 2 and 3.
"""

num_dict = {'1': '', '2': '', '3': ''}
for number in range(1, 11):
    result = str(number) + ', '
    if not number % 2:
        num_dict['1'] += result
    if not number % 3:
        num_dict['2'] += result
    if number % 2 and number % 3:
        num_dict['3'] += result

print(f"In the range from 1 to 10:\n"
      f"\t• even numbers that are divisible by 2: {num_dict['1'][:-2]};\n"
      f"\t• odd numbers, which are divisible by 3: {num_dict['2'][:-2]};\n"
      f"\t• numbers that are not divisible by 2 and 3: {num_dict['3'][:-2]}.")
