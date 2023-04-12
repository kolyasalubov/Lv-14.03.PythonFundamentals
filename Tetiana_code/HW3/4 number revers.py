num = 5794
prod = 1
rev = ''
num_sorted_result = ''
for c in str(num):
    prod = prod * int(c)
    rev = c + rev

for i in sorted(str(num)):
    num_sorted_result = num_sorted_result + i

print (prod)
print (int(rev))
print(num_sorted_result)