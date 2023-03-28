zen = '''The Zen of Python, by Tim Peters

1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!'''

print('Occurrences of the word "Better" in Zen of Python:',zen.count('better'))

print('Occurrences of the word "Never" in Zen of Python:',zen.count('never'))

print('Occurrences of the word "Is" in Zen of Python:',zen.count('is'))



print('\nZen of Python in uppercase:\n')

print(zen.upper())


print('\nZen of Python, but all "i" replaced with"&":\n')

print(zen.replace('i','&'))
