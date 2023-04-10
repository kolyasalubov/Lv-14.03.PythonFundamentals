def calculating_character(word):
    checked_letters = []
    result_dict = {}
    for letter in word:
        if letter not in checked_letters:
            result = word.count(letter)
            result_dict[letter] = result
            checked_letters.append(letter)
    return result_dict