import re

word = input("Enter your password: ")
az = re.search("[a-z]", word)
AZ = re.search("[A-Z]", word)
digit = re.search("[0-9]", word)
symbol = re.search("[$#@]", word)


def check_password():
    if az is None or AZ is None:
        return "At least 1 letter between [a-z] and 1 letter between [A-Z]."
    elif digit is None:
        return "At least 1 number between [0-9]."
    elif symbol is None:
        return "At least 1 character from [$#@]"
    elif len(word) < 6 or len(word) > 16 :
        return """Minimum length 6 characters.
Maximum length 16 characters."""
    else:
        return ("Password is correct")


print(check_password())