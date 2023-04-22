import random


user_name = input('Hello! What is your name?\n')


counter = 0
number = random.randint(1, 100)

print(f'Well, {user_name}, I am thinking of a number between 1 and 100.')


while True:

    guess_number = int(input('Take a guess! Enter your number: '))
    counter += 1

    if guess_number == number:
        print(f'Good job, {user_name}! You are a winner!!!')
        break

    elif 1 <= guess_number <= 100 and guess_number < number:
        print('Your number is less.')

    elif 1 <= guess_number <= 100 and guess_number > number:
        print('Your number is more.')

    elif not 1 <= guess_number <= 100:
        print(f"Your number is not in the range 1 to 100. Try again")

    if counter >= 10:
        print("Sorry guy, your attempts are done")
        break
