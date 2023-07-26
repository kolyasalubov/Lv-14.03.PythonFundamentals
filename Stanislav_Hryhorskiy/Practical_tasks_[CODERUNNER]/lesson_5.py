# QUESTION 1
# Create a function that takes a string and returns
# the number (count) of vowels contained within it.
# Notes
# a, e, i, o, u are considered vowels (not y).
# All test cases are one word and only contain letters.

def count_vowels(word):
    VOWELS = "aeiou"
    count = 0
    for letter in word.lower():
        if letter in VOWELS:
            count += 1
    return count


# QUESTION 2
# Create a function that returns the mean of all digits.
# The mean of all digits is the sum of digits / how many digits there
# are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=3).
# The mean will always be an integer.

def mean(number):
    mean_digits = 0
    for digit in str(number):
        mean_digits += int(digit)/len(str(number))
    return round(mean_digits)


# QUESTION 3
# Create a function which returns a list of booleans, from a given number.
# Iterating through the number one digit at a time, append True if the digit
# is 1 and False if it is 0.
# Notes. Expect numbers with 0 and 1 only.

def integer_boolean(binary_number):
    result_list = []
    for item in str(binary_number):
        if item:
            result_list.append(bool(int(item)))
    return result_list


# QUESTION 4
# Create a function that returns a base-2 (binary) representation of
# a base-10 (decimal) string number. To convert is simple: ((2) means
# base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
# Going from right to left, the value of the most right bit is 1,
# now from that every bit to the left will be x2 the value,
# value of an 8-bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
# Notes
# Numbers will always be below 1024 (not including 1024).
# The strings will always go to the length at which the most
# left bit's value gets bigger than the number in decimal.
# If a binary conversion for 0 is attempted, return "0".

def binary(decimal):
    if not decimal:
        return 0
    result = ""
    while decimal:
        result += str(decimal % 2)
        decimal //= 2
    return result[::-1]


# QUESTION 5
# An isogram is a word that has no duplicate letters.
# Create a function that takes a string and returns either
# True or False depending on whether it's an "isogram".
# Notes.
# Ignore letter case (should not be case-sensitive).
# All test cases contain valid one word strings.

def is_isogram(word):
    # return len(word.lower()) == len(set(word.lower()))
    for char in word.lower():
        if word.lower().count(char) > 1:
            return False
    return True
