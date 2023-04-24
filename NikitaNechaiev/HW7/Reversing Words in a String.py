def rev_word(word):
    word_r = word.split(' ')[-1::-1]
    word_r = ' '.join(word_r)
    return word_r

print(rev_word('hello how are you'))