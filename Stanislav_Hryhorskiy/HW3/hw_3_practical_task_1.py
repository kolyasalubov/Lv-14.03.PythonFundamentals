"""
*** Practical task 1 ***
You need to write Python's philosophy in the string format:
- find separately the number of occurrences of the words
"better", "never" and "is" in the given line;
- you need to display all text in uppercase (all letters in uppercase);
- replace all occurrences of the symbol "i" with "&".
"""

zen_python = """
1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules.
9. Although practicality beats purity.
10. Errors should never pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13. There should be one-- and preferably only one --obvious way to do it.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now is better than never.
16. Although never is often better than *right* now.
17. If the implementation is hard to explain, it's a bad idea.
18. If the implementation is easy to explain, it may be a good idea.
19. Namespaces are one honking great idea -- let's do more of those!
"""

line_number = int(input('Enter a number of line in \"The Zen of Python\" (from 1 to 19): '))

start_line = zen_python.find(str(line_number)) + len(str(line_number)) + 2
end_line = zen_python.find('\n', start_line)
line_text = zen_python[start_line:end_line]
words = "better", "never", "is"

print(f"\nText of aphorism №{line_number} (line {line_number}) of PEP 20 (The Zen of Python): {line_text}")
print(f"The number of occurrences of the word \"{words[0]}\" in the given line: {line_text.count(words[0])}")
print(f"The number of occurrences of the word \"{words[1]}\" in the given line: {line_text.count(words[1])}")
print(f"The number of occurrences of the word \"{words[2]}\" in the given line: {line_text.count(words[2])}\n")

print(f"Python's philosophy in uppercase:{zen_python.upper()}")

print(f"Python's philosophy after replace all occurrences of the symbol \"i\" with \"&\":"
      f"{zen_python.replace('i', '&')}")
