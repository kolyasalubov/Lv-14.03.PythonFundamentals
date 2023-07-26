# *** Task 4 ***
# Convert list containing miles to list containing
# kilometers (1 mile = 1.6 kilometers)
# a) using the map and some function
# b) using the map and lambda function

def convert_miles_to_km(value: float) -> float:
    """
    Function that convert value in 'miles' to 'kilometers'
    """
    return 1.6 * value


miles_list = [1, 2, 3, 4, 5]
# Variant 1 (using the map and some function)
kilometers_list = list(map(convert_miles_to_km, miles_list))
print(kilometers_list)

# Variant 2 (using the map and lambda function)
kilometers_list = list(map(lambda x: 1.6 * x, miles_list))
print(kilometers_list)

# Variant 3 (using the mlist comprehension)
kilometers_list = [1.6 * x for x in miles_list]
print(kilometers_list)
