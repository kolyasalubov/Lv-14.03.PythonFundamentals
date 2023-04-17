# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.


# r = range(11)
# parny = []
# neparny = []
# not_divisible_2_3 = []
# for n in r:
#     if n % 2 == 0:
#         parny.append(n)
#     elif n % 3 == 0:
#         neparny.append(n)
#     elif n % 2 != 0 and n % 3 != 0:
#         not_divisible_2_3.append(n)


# print("even numbers: ", parny)
# print("odd numbers: ", neparny)
# print("not divisible by 2 and 3: ", not_divisible_2_3)


############################# or ###########################
parny = set(n for n in range(11) if n % 2 == 0)
neparny = set(n for n in range(11) if n % 3 == 0 and n % 2 != 0)
not_divisible_2_3 = set(range(11))


print("even numbers: ", parny)
print("odd numbers: ", neparny)
print("not divisible by 2 and 3: ", not_divisible_2_3-parny-neparny)
