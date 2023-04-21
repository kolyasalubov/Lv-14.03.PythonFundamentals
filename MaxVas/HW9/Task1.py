from random import randint as r

user_attempts = 10
RANGE_MIN, RANGE_MAX, TOTAL_ATTEMPTS = 1, 100, user_attempts

computer_guess = r(RANGE_MIN, RANGE_MAX)

print('Hello friend! Lets play a game :)')

while user_attempts > 0:
    try:
        user_guess = int(input(f"Try to guess the number from {RANGE_MIN} to {RANGE_MAX}: "))
        if user_guess in range(RANGE_MIN, RANGE_MAX + 1):
            user_attempts -= 1
            if user_guess < computer_guess:
                print(f'Nice try! Your number is smaller than guessed one. Attempts left: {user_attempts}')
            elif user_guess > computer_guess:
                print(f'Nice try! Your number is greater than guessed one. Attempts left: {user_attempts}')
            else:
                print(f"You guessed the right number! Good job. You used {TOTAL_ATTEMPTS - user_attempts} tries.")
                break
        else:
            print("Please enter the number in correct range!!!")
            continue

    except ValueError as e:
        print(f"Error occured: {e} \nTry one more time.")
    
print(f"That was close! Number you tried to guess was {computer_guess}")
