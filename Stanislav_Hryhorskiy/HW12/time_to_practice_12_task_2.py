# *** Task 2 ***
# Display a list of list items that have the values "red",
# ["red","green", "black", "red", "brown", "red", "blue",
# "red", "red", "yellow"] using the filter function.

colors = ["red", "green", "black", "red", "brown",
          "red", "blue", "red", "red", "yellow"]

# Variant 1 (using the lambda function)
red_color = list(filter(lambda x: (x == "red"), colors))
print(red_color)


# Variant 2 (using some function)


def is_red(item: str):
    """
    Function that return "red" if item equal "red" otherwise returns None
    """
    if item == "red":
        return item


red_color = list(filter(is_red, colors))
print(red_color)
