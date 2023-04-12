our_string = input("Enter your string: ")


# Item 1: find separately the number of occurences of the words:
new_line = our_string.lower()
occur_better = new_line.count("better")
occur_never = new_line.count("never")
occur_is = new_line.count("is")
print(f"Occurences of the word 'beeter': {occur_better}\n"
      f"Occurences of the word 'never': {occur_never}\n"
      f"Occurences of the word 'is': {occur_is}")


# Item 2: display all text in uppercase:
print(our_string.upper())


# Item 3: replace all occurrences of the symbol "i" with "&":
print(our_string.replace("i", "&"))
