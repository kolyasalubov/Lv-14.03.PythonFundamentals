def reverse_words(string):

    words = string.split()

    words = words[::-1]

    reversed_string = ' '.join(words)
    return reversed_string

