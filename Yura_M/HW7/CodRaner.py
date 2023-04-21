# 1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# 2


def distance(x1, y1, x2, y2):
    b = (x1-x2)**2+(y1-y2)**2
    return round(b ** .5, 2)


# 3

def filter_words(st):
    b = st.split()
    m = ' '.join(b)
    return m.capitalize()

# 4


def number_to_string(num):
    return str(num)

# 5


def reverse(st):
    b = st.split()
    b.reverse()
    m = ' '.join(b)
    return m

# 6


def reverse_list(l):
    return l[::-1]


# 7


def solution(number):
    suma = 0
    for n in range(number):
        if n < 0:
            return 0
        if n % 3 == 0 or n % 5 == 0:
            suma = suma + n
    return suma

# 8


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False

# 9


def are_you_playing_banjo(name):
    for n in name[0:1]:
        if n == 'r' or n == 'R':
            return f"{name} plays banjo"
        else:
            return f"{name} does not play banjo"

# 10


def bool_to_word(bool):
    return "Yes" if bool else "No"

# 11


def count_sheeps(sheep):
    b = 0
    for n in sheep:
        if n == True:
            b += 1   
    return b 

# 12

def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False