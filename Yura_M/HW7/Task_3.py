# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

# def string_f(string):
#     """ Function that calculates the number
#     of characters included in given string
#     string: str
#     return: dictionary with the number of characters included in string
#     """
#     number = {}
#     for n in string:
#         if n not in number:
#             number[n] = 1
#         else:
#             number[n] += 1
#     return number


# word = string_f(str(input("enter your words: ")))

# print(word)


################################################################## HW 7 Task 3##############


def string_f(string):
    """ Function that calculates the number
    of characters included in given string
    string: str
    return: dictionary with the number of characters included in string
    """
    number = {}
    for n in string:
        if n not in number:
            number[n] = string.count(n)
    return number


if __name__ == "__main__":
    word = string_f(str(input("enter your words: ")))
    print(word)
