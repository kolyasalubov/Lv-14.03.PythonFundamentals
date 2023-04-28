# Jenny's secret message

def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
    

# Simple: Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    d = pow(((x2 - x1)**2 + (y2 - y1)**2), 0.5)
    return round(d, 2)

# No yelling!

def filter_words(st):
    return ' '.join(st.capitalize().split())

# Convert a Number to a String!

def number_to_string(num):
    return str(num)

# Reversing Words in a String

def reverse(st):
    return ' '.join(st.split()[::-1])

# Reverse List Order

def reverse_list(l):
    return l[::-1]

# Multiples of 3 or 5

def solution(number):
    numbers = [n for n in range(number) if n % 3 == 0 or n % 5 == 0]
    return sum(numbers)

# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

# Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
# Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

# Counting sheep...

def count_sheeps(sheep):
    counter = 0
    for sh in sheep:
        if sh == True:
            counter += 1
    return counter

# Is this my tail?

def correct_tail(body, tail):
    return body[-1] == tail[0]

