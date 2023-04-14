def numbers_chars(word: str) -> dict:
    dict_characters = set(word)
    amount_chars = {}
    for item in dict_characters:
        result = word.count(item)
        numbers = dict([(item, result)])
        amount_chars.update(numbers)

    return amount_chars


amount = numbers_chars(word=input("Enter your word please:"))
print(f"Here's your amount of letters in the word:\n{amount}")
