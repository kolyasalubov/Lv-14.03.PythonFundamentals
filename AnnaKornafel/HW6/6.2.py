while True:
    login = input('Enter a login: ')
    if login == 'First':
        print(f'Greetings! You are entered as - {login}.')
        break
    elif login != 'First':
        print('Error. Try again.')