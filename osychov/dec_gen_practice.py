# from functools import reduce

#1
# names  = ['Sam', 'Don', 'Daniel']
# print(list(map(hash, names)))

#2
# ls =  ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
# print(list(filter(lambda x: x == "red",ls))) 

#3
# ls = ['1', '2', '3', '4', '5', '6']
# print([int(x) for x in ls])
# print(list(map(int, ls)))

#4
# def miles_to_kil(item):
#     return (item * 1.6).__round__(2)

# ls_miles = [1, 2, 3, 4, 5, 6, 7]
# ls_kilom = list(map(lambda item : (item * 1.6).__round__(2), ls_miles))
# print(ls_kilom)
# ls_kilom = list(map(miles_to_kil, ls_miles))
# print(ls_kilom)

#5
# ls = [1, 2, 3, 4, 5, 6]

# ls_reduce = reduce(max, ls, 0)
# print(ls_reduce)
# ls_reduce = reduce(lambda x, y : x if (x > y) else y, ls, 0)
# print(ls_reduce)

#6
# gener = (x for x in range(5))
# for i in gener:
#     print(i)


#7
def sandwich(func):
    def inner(*args):
        print("<\ ^^^^^^^ />")
        for i in args:    
            if i == "tomatoes" :
                print("# tomato #")
            elif i == "meat":
                print("-meat-")
            elif i == "lettuce" :
                print("~ salad ~")  
        print("<\ ______ />")
    return inner

@sandwich
def sandwich_creater(*args):
    pass

sandwich_creater("lettuce", "tomatoes", "meat")
