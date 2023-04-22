import random

def guess_number():
    random_number = random.randint(1, 100)
    tries = 10
    while tries != 0:
        user_number = int(input("Enter number: "))
        if user_number == random_number:
            print("You guessed the number. Congratulations!")
            break
        else:
            if user_number > random_number:
                print("The number I guessed is less than yours!")
            else:
                print("The number I guessed is more than yours!")
        tries-=1
        print(f"You have {tries} attempts left")
    else:
        print(f"Unfortunately, the attempts are over. The number I guessed: {random_number}")

if __name__ == "__main__":
    guess_number()