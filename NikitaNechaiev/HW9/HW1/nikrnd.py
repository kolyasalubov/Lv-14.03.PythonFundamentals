def randomnum():
    import random
    from input_name import u_name
    number = random.randint(1,100)
    max_guesses = 10
    num_guesses = 1
    while num_guesses <= max_guesses:
        # print(number)
        guess_int = int(input(f'Attempt №{num_guesses} of {max_guesses}\nGuess the number: '))
        num_guesses += 1
        if guess_int == number:
            print('Congrats %s!\nYou are a winner!'%u_name) 
            break
        elif 1 < guess_int < 100 and guess_int < number:
            print('%s your number is less!'%u_name)
        elif 1 < guess_int < 100 and guess_int > number:
            print('%s your number is more!'%u_name)
        elif not 1 <= guess_int <= 100:
            print("%s your number is not in the range 1 to 100.\nTry again:)"%u_name)
    print('%s you reached out of attempts.\nThe guessed number was %s.'%(u_name,number))
randomnum()
