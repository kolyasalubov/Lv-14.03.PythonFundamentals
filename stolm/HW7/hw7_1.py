def bigger(num1, num2):
    """
    We compare two numbers: if the first number is greater
    than the second, we return it. Otherwise, we return
    the second number.
    """
    if num1 > num2:
        return num1
    else:
        return num2


if __name__ == "__main__":
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(bigger(num1, num2))
    print("DocString: ", bigger.__doc__)

