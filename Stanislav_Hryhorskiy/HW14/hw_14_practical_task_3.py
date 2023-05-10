# *** Task 3 ***
# Write a function to find the square of the rectangle
# and write an unittest for this function.


def get_area_rectangle(length: int | float, width: int | float) -> str:
    """
    Function that calculate area of the rectangle
    :param length: int | float
    :param width: int | float
    :return: message about the result of calculating the area of a rectangle
    """
    if not isinstance(length, int | float) or not isinstance(width, int | float):
        raise TypeError("Length and width of rectangle must be float type!")
    if length <= 0 or width <=0:
        return "Length and width of rectangle must be non-negative numbers!"
    area = length * width
    return f"S = {area} square units."


if __name__ == "__main__":
    print(get_area_rectangle(-6.8, 5))
