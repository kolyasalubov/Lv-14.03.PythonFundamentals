# #1
# def celsius_to_fahrenheit(temps):
#     temp_farenheit = [(C * 9/5) +32  for C in temps]
#     return temp_farenheit

# celsius_temperatures = [0, 10, 20, 30, 40]
# print(celsius_to_fahrenheit(celsius_temperatures))

#2
# def celsius_to_fahrenheit(temps):
#     return list(map(lambda x :(x * 9/5) + 32, temps))


# celsius_temperatures = [0, 10, 20, 30, 40]
# print(celsius_to_fahrenheit(celsius_temperatures))
    
#3
# def add_tag(tag):
#     def decorator(func):
#         def adding(*args, **kwargs):
#             word = func()
#             return tag+word+tag
#         return adding
#     return decorator
    
    

# @add_tag("<strong>")
# def get_message():
#     return "Hello, World!"

# print(get_message())

#4

# def combinations(list1, list2):
#     result = []
#     for i in list1:
#         for u in list2:
#             result.append((i, u))
#     res = (x for x in result)
#     return res

# def combinations(list1, list2):
#     for i in list1:
#       for u in list2:
#         yield i, u

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# for combination in combinations(list1, list2):
#     print(combination)

#5

# def fibonacci_numbers():
#     num1 = 0
#     num2 = 1
#     yield num1
#     yield num2
#     while True: 
#         num1, num2 = num2, num1+num2
#         yield num2
    
    
# fib = fibonacci_numbers()
# for i in range(10):
#     print(next(fib))



# def lists(list1, list2):
#     keys = list1
#     values = list2
#     return {key: value for (key, value) in zip(keys, values)}
# print(lists([1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 4, 5]))
  
