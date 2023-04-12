# 1 TASK---------------------------------------------

li = [1, 2, 3, 4, 5]

for i in li:
    chan = float(li[i])
    print(chan, type(chan))

print(type(li[1]))

# 2 TASK---------------------------------------------


#
#
#
# li1 = [0, 1]
# for i in li1:
#     if i < 10:
#         fib = li1[i] + li1[i+1]
#         add = li1.append(fib)
#         print(i, i+1, li1[i], li1[i + 1], li1)
#     else:
#         print("done")

# print(li1)


n = int(input("Write down your number: "))

li1 = [0, 1]
fib = 0
for i in range(n):
    if fib < n:
        fib = li1[i] + li1[i+1]
        addd = li1.append(fib)
        # print(i)
    else:
        break
print(li1[:-1])

# 3 TASK------------------------------------------ori---
#
# factorial = int(input("enter your factorial: "))
# list = [0, 1]
#
# if factorial >= 0:
#     for i in range(factorial):
#         fact = list[-1] * (i+1)
#         # print(fact)
#         list.append(fact)
#     print(f"your result is {list[-1]}")
# else:
#     print("error, your number {} cannot be used".format(factorial))

factorial = int(input("enter your factorial: "))

result = 0
i = 0
count = 1
if factorial > 0:
    while i < factorial:
        result = (factorial - i) * count
        i += 1
        count = result
    print(result)
elif factorial == 0:
    print("1")
else:
    print("error")
