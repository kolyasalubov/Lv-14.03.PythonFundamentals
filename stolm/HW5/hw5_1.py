N = int(input("Enter size of list: ")) # Get size of our list
my_list = [int(input("Enter element: ")) for i in range(N)] # Create our list
myfloat_list = []

# For loop to add float elements to the myfloat_list
for i in my_list:
    myfloat_list.append(float(i))

# Print lists
print(f"Our head list : {my_list}")
print(f"Our float list : {myfloat_list}")