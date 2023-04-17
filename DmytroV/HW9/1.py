import random

number = random.randint(1, 100)
amount_attempts = 0
maximum_attempts = 10

user_name = input ("Hello! What is your name? ")

while True:
    if amount_attempts == maximum_attempts:
        print(f"Your amount of attempts is {amount_attempts}. Your game is finish")
        break
    else: 
        amount_attempts != maximum_attempts
        guess_number = int(input (f"{user_name} enter a number in range from 1 to 100: "))
        amount_attempts += 1
        if guess_number == number:
            print(f"{user_name} congratulate! You are winner!")
        if 1 <= guess_number <= 100 and guess_number < number:
            print(f"{user_name} your input number is less than the number you are looking for!\
            Try again. You still have {maximum_attempts-amount_attempts} tries")
        if 1 < guess_number < 100 and guess_number > number:
            print(f"{user_name} your input number is grater than the number you are looking for\
            Try again. You still have {maximum_attempts - amount_attempts} tries")
        
        #довго не міг зрозуміти чому не відпрацьовував код нижче, якщо число було не в деапозоні
        #Потім методом тику після if вставив not і спрацювало, але так і не зрозумів чому
        if not 1 > guess_number > 100:
            print(f"{user_name} your entered number not in range! Try again!\
            You still have {maximum_attempts - amount_attempts} tries")
    
        
    

