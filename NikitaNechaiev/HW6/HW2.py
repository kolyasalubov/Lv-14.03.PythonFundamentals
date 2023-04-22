while True:
    login = input('Enter a login: ')
    if login == 'First':
        print(f'Greetings!\nYou are entered as - {login}.')
        break
    elif login != 'First':
        print('Login is not defined. \nTry again.')
