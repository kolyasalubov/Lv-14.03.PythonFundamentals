# *** Task 1 ***
# Rewrite the following code through using the map function.
# The function takes a list of real names and replaces them
# with the appropriate hash combinations using the hashing method.

# Variant 1 (using for loop)
names = ['Sam', 'Don', 'Daniel']
for i in range(len(names)):
    names[i] = hash(names[i])
print(names)

# Variant 2 (using the map function)
names = ['Sam', 'Don', 'Daniel']
names = list(map(hash, names))
print(names)
