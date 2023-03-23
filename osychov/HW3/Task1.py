file = open("Zen.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
string = """Zen of Python!!!
1. 
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7.
8. Special cases aren't special enough to break the rules.
9.  Although practicality beats purity.
10. Errors should never pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now is better than never.
16. Although never is often better than *right* now.
17. If the implementation is hard to explain, it's a bad idea.
18. If the implementation is easy to explain, it may be a good idea.
19. Namespaces are one honking great idea -- let's do more of those!
20.
21. Explicit is better than implicit.
22. Simple is better than complex.
23.Complex is better than complicated.
24. Flat is better than nested.
25. Sparse is better than dense.
26.
27. Special cases aren't special enough to break the rules.
28. Although practicality beats purity.
29. Errors should never pass silently.
30. Unless explicitly silenced.
31.
32.
33.Although that way may not be obvious at first unless you're Dutch.
34.
35. Although never is often better than *right* now.
36. If the implementation is hard to explain, it's a bad idea.
37. If the implementation is easy to explain, it may be a good idea.
38. Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
39.Explicit is better than implicit."""
better = lines.count("better")
never = string.count("never")
is1 = string.count("is")
print(f"Occurence in better - {better}, never - {never}, is - {is1}")

print(string.upper())

print(string.replace("i", "&"))

