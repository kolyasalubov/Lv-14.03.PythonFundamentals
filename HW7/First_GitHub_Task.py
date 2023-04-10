def largest_num(num1: int, num2: int) -> int:
    """
    Doc string:
    input params: num1, num2;
    type1: num1 = int;
    type2: num2 = int;
    output: num1 > num2, or num2> num1;
    type3: output = int.
    """
    if num1 > num2:
        return num1
    else:
        return num2


largest = largest_num(num1=int(input("Put first number please:")),
                      num2=int(input("Put second number please:")))
print("The largest number is:", largest)
print(largest_num.__doc__)
