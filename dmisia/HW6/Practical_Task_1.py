num2 = [i for i in range(1,11) if i % 2 == 0]
num3 = [i for i in range(1,11) if i % 2 == 1 and i % 3 == 0]
num2_3 = [i for i in range(1,11) if i % 2 != 0 and i % 3 != 0]

print(f"Even numbers that are divisible by 2: {num2}\n" 
      f"Odd numbers that are divisible by 3: {num3}\n"
      f"Numbers that are divisible not divisible by 2 and 3: {num2_3}")