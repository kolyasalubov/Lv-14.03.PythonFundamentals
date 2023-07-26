import re


while True:
    pasword = input("Enter your pasword: ")
    lowLetter = re.findall('[a-z]', pasword)
    lowLetter = len(lowLetter)
    bigLetter = re.findall('[A-Z]', pasword)
    bigLetter = len(bigLetter)
    number = re.findall('[0-9]', pasword)
    number = len(number)
    character = re.findall('[$#@]', pasword)
    character = len(character)
    if len(pasword) >= 6 and len(pasword) <= 16:
        if character >= 1 and number >= 1:
            if lowLetter >= 1 and bigLetter >= 1:
                print("Congratulations, your password is valid!")
                break
    else:
        print("Sorry your password is invalid. Try again!")
