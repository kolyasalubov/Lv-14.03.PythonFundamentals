# QUESTION 1
# Create a function that takes a list and finds
# the list of integers that appear an odd number of times.

def find_odd(lst):
    res_set = set()
    for item in lst:
        if lst.count(item) % 2 and item not in res_set:
            res_set.add(item)
    return list(res_set)


# QUESTION 2
# Given an unsorted list, create a function that returns the nth smallest
# integer (the smallest integer is the first smallest, the second smallest
# integer is the second smallest, etc).
# Notes
# n will always be >= 1.
# Each number in the array will be distinct (there will be a clear ordering).
# Given an out of bounds parameter (e.g. a list is of size k), and you are
# asked to find the m > k smallest integer, return None.

def nth_smallest(lst, n):
    lst.sort()
    if n <= len(lst):
        return lst[n - 1]


# QUESTION 3
# Given a list of numbers and a value n, write a function that returns
# the probability of choosing a number greater than or equal to n from
# the list. The probability should be expressed as a percentage, rounded
# to one decimal place.
# Notes. Percent probability of event = 100 * (num of favourable outcomes) /
# (total num of possible outcomes)

def probability(lst, num):
    fav_num = 0
    for item in lst:
        if item >= num:
            fav_num += 1
    return round(100 * fav_num / len(lst), 1)


# QUESTION 4
# Create a function that takes a list of non-negative integers
# and strings and return a new list without the strings.
# Notes
# Zero is a non-negative integer.
# The given list only has integers and strings.
# Numbers in the list should not repeat.
# The original order must be maintained.

def filter_list(lst):
    new_lst = []
    for item in lst:
        if isinstance(item, int):
            new_lst.append(item)
    return new_lst


# QUESTION 5
# Given a list of numbers, create a function which returns
# the list but with each element's index in the list added
# to itself. This means you add 0 to the number at index 0,
# add 1 to the number at index 1, etc...

def add_indexes(lst):
    new_lst = []
    for index, value in enumerate(lst):
        new_lst.append(index + value)
    return new_lst
