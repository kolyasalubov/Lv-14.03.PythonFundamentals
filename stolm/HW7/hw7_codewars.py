# I. Jenny's secret message : 
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else: 
#         return f"Hello, {name}!"


# II. Fint The Distance Between Two Points : 
# from math import sqrt
# def distance(x1, y1, x2, y2):
#     return round(sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)), 2)

# III. No yelling! :
# def filter_words(st):
#     st = " ".join(st.split())
#     st = st.rstrip()
#     return st.capitalize()


# IV. Convert a number to a string :
# def number_to_string(num):
#     return str(num)


# V. Reversing Words in a String :
# def reverse(st):
#     st = st.split()
#     st = st[::-1]
#     str=" "
#     return str.join(st)


# VI. Reverse List Order :
# def reverse_list(l):
#     return l[::-1]


# VII. Multiplies of 3 or 5 : 
# def solution(number):
#     if number < 0:
#         return 0
#     else:
#         sum = i = 0
#         for i in range(number):
#             if i % 3 == 0 or i % 5 == 0:
#                 sum+=i
#     return sum


# VIII. Will you make it? :
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump <= mpg*fuel_left:
#         return True
#     return False


# IX. Are You Playing Banjo? : 
# def are_you_playing_banjo(name):
#     if name.lower()[0] == "r":
#         return name + " plays banjo"
#     return name + " does not play banjo"


# X. Convert boolean values to string 'Yes' or 'No' : 
# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     return "No"


# XI. Counting sheep : 
# def count_sheeps(sheep):
#     counter = 0
#     for i in sheep:
#         if i == True:
#             counter+=1
#     return counter


# XII. Is this my tail? : 
# def correct_tail(body, tail):
#     if tail == body[-1]:
#         return True
#     return False
