login = input('Hello, enter login: ')
while login != 'First':
    login = input('Error: try again. Login: ')
else:
    print(f'Hello, {login}!')
