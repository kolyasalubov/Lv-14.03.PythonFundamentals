def password_validator(password):
    has_digits = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    specials = ['$', '#', '@']
    has_specials = any(char in specials for char in password)
    
    match password:
        case too_short if len(password) < 6:
            return print('Password is too short. Minimum lenght is 6 characters.')
        case too_long if len(password) > 16:
            return print('Password is too short. Maximum lenght is 16 characters.')
        case no_digits if not has_digits:
            return print('Password has no digits. You need at least one.')
        case no_lower if not has_lower:
            return print('Password has no lowercase characters. You need at least one.')
        case no_upper if not has_upper:
            return print('Password has no uppercase characters. You need at least one.')
        case nu_symbols if not has_specials:
            return print('Password has no special symbols. You need at least one')
        case all_good:
            return True
        

if __name__ == '__main__':
    password = input('Enter your password: ')
    while password_validator(password) != True:
        password = input('Try again: ')
    else:
        print('Your password is confirmed. ')

