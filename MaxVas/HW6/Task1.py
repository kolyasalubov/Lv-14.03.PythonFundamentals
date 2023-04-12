print(f"""Odd numbers divisible by 3: {[i for i in range(1, 10) if i % 3 == 0]}
Even numbers divisible by 2: {[i for i in range(1, 10) if i % 2 == 0]}
Not divisible numbers by 2 and 3: {[i for i in range(1, 10) if i % 3 != 0 and i % 2 != 0]}""")