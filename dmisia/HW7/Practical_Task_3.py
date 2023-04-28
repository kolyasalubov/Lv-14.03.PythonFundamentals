def calc(word):
    dict1 = {}
    for i in word:
        dict1[i] = word.count(i)
    return dict1
word = input("Enter your word: ")