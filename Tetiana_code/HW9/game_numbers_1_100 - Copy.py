import random

number_to_guess = random.randint(1, 100)

max_attempt = 10
attempt = 0

guessed = False

while attempt < max_attempt and not guessed:
    answer = int(input("Enter the number (between 1 and 100): "))
    
    if answer == number_to_guess:
        guessed = True
        print("Congratulations, your answer is correct")
    elif answer < number_to_guess:
        print("The number is greater than your answer.")
    else:
        print("The number is less than your answer.")
    
    attempt += 1

if not guessed:
    print("Sorry, your attemts are over. The correct number", number_to_guess)
