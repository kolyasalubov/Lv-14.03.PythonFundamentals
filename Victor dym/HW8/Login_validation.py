import re
password = input("Enter your password: ")




def check_password():
    check_for_a_z = re.findall('[a-z]', password)
    check_for_A_Z = re.findall("[A-Z]", password)
    check_for_signs = re.findall("[#$@]", password)
    length = len(password)

    if length >= 6 and length <= 16:
        if check_for_a_z and check_for_A_Z and check_for_signs:
            print(password)

check_password()