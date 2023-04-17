def counter_letters(word):
    letter_counts = {letter: word.count(letter) for letter in word}
    return letter_counts


if __name__=="__main__":
    word=input("Enter your word: ")
    print(counter_letters(word))