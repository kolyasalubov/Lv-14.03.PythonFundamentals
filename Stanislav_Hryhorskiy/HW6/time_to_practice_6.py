"""
Create a list of integers that are entered from the terminal
and determine the maximum and minimum number among them.
"""

# num_list = list(map(int, input("Enter integers separated by spaces: ").split()))
num_list = [int(input(f"Enter the number that will be in the list (index {number}): "))
            for number in range(int(input("Enter the length of the list: ")))]

print()
print(f"There are a total of {len(num_list)} integers in the entered list:\n"
      f"\t-the minimum number in the list is {min(num_list)};\n"
      f"\t-the  maximum number in the list is {max(num_list)}.")
print()

min_num = max_num = num_list[0]
count = 0
for item in num_list:
    if min_num > item:
        min_num = item
    if max_num < item:
        max_num = item
    count += 1

print(f"There are a total of {count} integers in the entered list:\n"
      f"\t-the minimum number in the list is {min_num};\n"
      f"\t-the  maximum number in the list is {max_num}.")
