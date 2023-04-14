# *** Practical task 3 ***
# Write a function that calculates the number
# of characters included in given string.

def get_num_repeat(phrase: str) -> dict:
    """
    Function that calculates the number
    of characters included in given string
    :param phrase: str
    :return: dictionary with the number of characters included in phrase
    """
    result_dict = {}
    for char in phrase:
        if not result_dict.get(char):
            result_dict[char] = phrase.count(char)
    return result_dict


if __name__ == "__main__":
    string = input("Enter an arbitrary string: ")
    print(get_num_repeat(string))
