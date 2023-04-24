# *** Practical task 2 ***
# Write a Python program to check the validity
# of a password (input from users). Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

MIN_LENGTH, MAX_LENGTH = 6, 16

pattern = [re.compile(r"[a-z]+"),
           re.compile(r"[A-Z]+"),
           re.compile(r"\d+"),
           re.compile(r"[$#@]+"),
           re.compile(r"^[a-zA-Z0-9$#@]{6,}$"),
           re.compile(r"^[a-zA-Z0-9$#@]{,16}$")]

comment = ["Password must contain at least 1 letter between [a-z]!",
           "Password must contain at least 1 letter between [A-Z]!",
           "Password must contain at least 1 number between [0-9]!",
           "Password must contain at least 1 character from [$#@]!",
           f"The minimum password length is {MIN_LENGTH} characters!",
           f"The maximum password length is {MAX_LENGTH} characters!"]

while True:
    password = input("Enter your password: ")
    for item in range(6):
        if not pattern[item].search(password):
            print(comment[item])
            break
    else:
        print("Congratulations! Your password has been validated.")
        break
