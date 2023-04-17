import random

num = random.randint(1, 100)
attempts = 0
while True:
    guessed_num = int(input("Guess th number in range from 1 to 100:"))
    if guessed_num > num:
        print("Your number is too large. Try again.")
        attempts += 1
    elif guessed_num < num:
        print("Your number is too small. Try again.")
        attempts += 1
    elif attempts == 10:
        print("Sorry, but you have wasted all your attempts. You lost.")
    elif guessed_num == num:
        print("Congratulations! You won!")