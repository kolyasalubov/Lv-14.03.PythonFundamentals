# from itertools import zip_longest

# numbs = [10,20,30,50,60]
# symbs = ['h', 'y' ,'i']
# numbs2 = [1,2,3]

# for i in zip_longest(numbs,symbs,numbs2):
#     print(i)

# winning_lottery_numbers = [0, 4, 3, 2, 3, 1]

# fake_lottery_numbers = [2*n for n in winning_lottery_numbers]
# print(fake_lottery_numbers)


# fake_lottery_numbers_2 = map(lambda n: 2*n, winning_lottery_numbers)
# print(fake_lottery_numbers_2)
# for item in fake_lottery_numbers_2:
#     print(item)

# names = ['Sam', 'Don', 'Daniel']
# new_names = list(map(hash,names))
# print (new_names)

# for i in range(len(names)):
#     names[i] = hash(names[i])
#     print(names)  


# def isPos(number):
#     return number > 0

# numbs = [-1,2,3,-4,-5,6,7,-8,9]
# result = list(filter(lambda x: not isPos(x), numbs))
# print(result)
# def show_res(color):
#     if color == 'red':
#         return color



# cls = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", 'yellow']
# res = list(filter(lambda x:show_res(x),cls))
# print(res)


# All these numbers in the list have a string data type, for example ['1', '2', '3', '4', '5', '7'],
# convert this list to a list, all numbers of which have the data type integer : 
# using the append method 
# using the map method



# numbs = ['1', '2', '3', '4', '5', '7']
# # res = list(map(int,numbs))
# # print(res)
# start = []
# for i in numbs:
#     start.append(int(i))
# print(start)


# d = [10]
# res = list(map(lambda x: x*1.6,d))
# print(res)



# def counter(number):
#     return 1.6 * number


# d = [10]
# res = list(map(counter,d))
# print(res)

# from functools import reduce

# spisok = [43,1,12,121,-4,23]
# res = reduce(lambda a,b: a if (a > b) else b, spisok )
# print(res)

 
