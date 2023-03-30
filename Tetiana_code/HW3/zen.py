

sentence = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one and preferably only one obvious way to do it.
Although that way may not be obvious at first unless youre Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea – lets do more of those!"""
word1 = "better"
word2 = "never"
word3 = "is"
char = "i"
list = sentence.upper().split()
word1_count = 0
word2_count = 0
word3_count = 0

for w in list:
    if w == word1.upper():
        word1_count = word1_count + 1
    if w == word2.upper():
        word2_count = word2_count + 1
    if w == word3.upper():
        word3_count = word3_count + 1

print(sentence.upper().replace("I","&"))

print(f"{word1_count=}")
print(f"{word2_count=}")
print(f"{word3_count=}")

