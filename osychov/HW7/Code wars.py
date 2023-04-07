# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)


# import math
# def distance(x1, y1, x2, y2):
#     # length = math.sqrt((y2-y1)^2 + (x2-x1)^2)
#     dist = math.hypot(x2 - x1, y2 - y1).__round__(2)   ##Найти гипотенузу hypot(a, b)
#     return dist


# def filter_words(st):
#     string = st.strip(" ").capitalize()
#     return string


# def number_to_string(num):
#     return str(num)


# def number_to_string(num):
#     try:
#         return str(num)
#     except:
#         return None


# def reverse(st):
#     lt = st.split()
#     return f"{lt[1]}{lt[0]}"
# cum = "string cum."
# print(reverse(cum))


# def reverse_list(l):
#   l.reverse()
#   return l


# def solution(number):
#     ls = []
#     if number < 0:
#         return 0
#     for i in range(0, number):
#         if i % 3 == 0 or i % 5 == 0:
#             ls.append(i)
#     return sum(ls)

    #   return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# def solution(number):
#     sum = 0
#     if number < 0:
#         return 0
#     for i in range(0, number):
#         if i % 3 == 0 or i % 5 == 0:
#             sum+=i
#     return sum

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump <= mpg * fuel_left:
#         return True
#     else:
#         return False


# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'


# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"


# def count_sheeps(sheep):
#   sum = 0 
#   for item in sheep:
#       if item:
#           sum+=1
#   return sum


# def count_sheeps(arrayOfSheeps):
#   return arrayOfSheeps.count(True)


# def correct_tail(body, tail):
#     sub = body[-1]
#     if sub == tail:
#         return True
#     else:
#         return False


# def correct_tail(body, tail):
#     return body[-1] == tail

# def filter_words(st):
#     return " ".join(st.split()).capitalize() 