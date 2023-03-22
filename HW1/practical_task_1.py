"""
WRITE A PROGRAM THAT WILL DISPLAY THE FOLLOWING QUESTIONS FOR USER:
      “WHAT IS YOUR NAME?“
       “HOW OLD ARE YOU?“
       “WHERE DO YOU LIVE?“
and will read the user's responses and display the corresponding messages:
      “HELLO, (ANSWER(NAME))“.
      “YOUR AGE IS  (ANSWER(AGE))“.
      “YOU LIVE IN  (ANSWER(CITY))“.
"""

name = input('WHAT IS YOUR NAME?   ').upper()
age = int(input('HOW OLD ARE YOU?     '))
city = input('WHERE DO YOU LIVE?   ').upper()

print()
print('HELLO,', name)
print('YOUR AGE IS', age)
print('YOU LIVE IN', city)
