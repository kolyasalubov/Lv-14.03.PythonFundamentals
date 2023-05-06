import random
from random import *

randomize_int = randint(1, 100)
for i in range(1, 11):
    entered_int = int(input("Enter your number: "))
    if entered_int == randomize_int:
        print("You guessed right ")
        break
    elif entered_int != randomize_int and i == 10:
        print("You didn't guess(((( ")
    elif entered_int > randomize_int:
        print("the randomize num is lower, try again ")
        # continue
    elif entered_int < randomize_int:
        print("the randomized num is higher, try again ")
        # continue
