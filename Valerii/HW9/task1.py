from random import randint
""" The game script that randomly generates a number from a range of 
1 to 100 and asks the user to guess that number in 10 tries.
"""
number = randint(1, 100)

counter = 10
guessed_number = int(input(f'Guess the number in range of 1 to 100.\n You have {counter} tries. \n number = '))
while guessed_number != number:
    counter -= 1
    if counter == 0:
        print('You lost the game. Sorry...')
        break
    if guessed_number > number:
        print('Your number is higher then mine.')
    elif guessed_number < number:
        print('Your number is lower then mine.')
    guessed_number = int(input(f'Try again. {counter} tries left. \n number:'))
else:
    print('Congratulations! You won!')