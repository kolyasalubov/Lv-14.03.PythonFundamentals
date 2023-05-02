# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return f"Hello, {name}!"


# def distance(x1, y1, x2, y2):
#     d = ((x2 - x1)**2+(y2 - y1)**2)**0.5
#     return round(d,2)


# def filter_words(st):
#     st = st.capitalize()
#     st = st.split()
#     st = ' '.join(st) 
#     return st

# def number_to_string(num):
#     return str(num)


# def reverse(st):
#     st = st.split()
#     st.reverse()
#     st = ' '.join(st)
#     return st


# def reverse_list(l):
#   l.reverse()
#   return l


# def solution(number):
#     l = []
#     for i in range(number):
#         if i%3 == 0:
#             l.append(i)
        
#         elif i%5 == 0:
#             l.append(i)
#     s = sum(l)    
#     return s

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if mpg*fuel_left >= distance_to_pump:
#         return True
#     else:
#         return False


# def are_you_playing_banjo(name):
    
#     if name[0] == 'r' or name [0] == 'R':
#         answ = ' plays banjo'    
#     else:
#         answ = ' does not play banjo'
#     return name + answ


# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     elif boolean == False:
#         return "No"


# def count_sheeps(sheep):
#     count = 0
#     for i in sheep:
#         if i == True:
#             count += 1
#     return count


# def correct_tail(body, tail):
#     if body[-1] == tail:
#         return True
#     else:
#         return False