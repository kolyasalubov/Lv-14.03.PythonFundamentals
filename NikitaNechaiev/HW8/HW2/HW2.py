import re
while True:
    password = input('Welcome user!\nEnter a password:\n')
    if  len(password) < 6 or len(password) > 16:
        print('%s is not a valid password\nMinimum length 6 characters.\nMaximum length 16 characters.'%password)
    elif not re.search('[a-z]',password) or not re.search('[A-Z]',password):
        print('%s is not a valid password\nAt least 1 letter between [a-z] and 1 letter between [A-Z].'%password)
    elif not re.search('[0-9]',password):
        print('%s is not a valid password\nAt least 1 number between [0-9].'%password)
    elif not re.search('[$#@]',password):
        print('%s is not a valid password\nAt least 1 character from [$#@].'%password)
    else:
        print('%s is valid password.' %password)










# check_symb = ['$','#','@']
# check_num = ['0','1','2','3','4','5','6','7','8','9']
# check_letter = ['A','a','B','b', 
#          'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H' ,'h', 'I', 
#          'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o',
#          'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U' ,'u', 'V',
#          'v', 'W', 'w', 'X', 'x', 'Y' ,'y' ,'Z' ,'z']