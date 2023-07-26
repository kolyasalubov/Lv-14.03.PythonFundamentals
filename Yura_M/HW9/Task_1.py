import random

number = random.randint(1, 100)

num_guesses = 0

while num_guesses < 10:

    guess = int(input('Enter a number between 1 and 100: '))
    num_guesses += 1

    if guess == number:
        print('Congratulations, you guessed the number in', num_guesses, 'tries!')
        break
    if guess < number:
        print('Your guess is too low.')
    else:
        print('Your guess is too high.')

if num_guesses == 10:
    print('Sorry, you did not guess the number. The number was', number)
