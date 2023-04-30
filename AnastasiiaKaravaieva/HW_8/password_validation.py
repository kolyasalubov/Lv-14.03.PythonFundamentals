import re


def validation(passwrd):
    reg = "[A-Za-z\d@$#]{6,16}$"
    pat = re.compile(reg)

    # searching regex
    mat = re.search(pat, passwrd)

    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid!")


validation(input("Write your password:"))