# First assignment

py_zen = input("Write your favourite Python's Zen line:")

low_string = py_zen.lower()

print(f"""quantity of better occurrence:{low_string.count('better')}\n"""
      f"""quantity of never occurrence:{low_string.count('never')}\n"""
      f"""quantity of is occurrence:{low_string.count('is')}""")

# Second assignment
upper_string = py_zen.upper()

print(f"Your line in a upper view: {upper_string}")

# Third assignment
replace_string = py_zen.replace('i', '&')

print(f"Your line with a little change: {replace_string}")