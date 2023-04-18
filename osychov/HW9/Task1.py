import random

def check_input_number():
    number = random.randint(1, 100)
    attempt = 1
    while attempt <= 10:
        inp = int(input(f"Attempt {attempt}: "))
        if inp in range(1, 101):
            if inp == number:
                print("You're guessed!!!")
            else:
                print("Not correct, maybe next attempt....")
                attempt+=1
        else:
            print("Number must be from 1 to 100!")
            attempt+=1
            
    else:
        print("You're not guessed for 10 times :(")

check_input_number()