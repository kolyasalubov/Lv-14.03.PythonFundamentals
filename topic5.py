#while
############################

# i = 5
# while i <= 15:
#     print(i)
#     i = i + 2

##################
# for
##################


# for i in 'hello world':
#     print(i*2, end='№')
#     print(i * 2)


#у вище вказаному прикладі функція print() має 
# також аргумент end — він вказує, яким символом 
# має закінчуватись поточне виведення на екран. 
# Якщо в функції print() не вказаний даний аргумент 
# то виведення закінчується символом переходу на 
# нову стрічку (\n).
#for
#
# spisok = [10, 40, 20, 30]
# for element in spisok:
#     print(element + 2)
# print(spisok)
# ##for

# spisok = [10, 40, 20, 30]
# i = 0
# for element in spisok:
#      spisok[i] = element + 2
#      i += 1
#      print(element)
# print(spisok)


######################
#for для dictionary
######################

# d = {1:'one',2:'two',3:'three',4:'four'}
# for key in d:
#     d[key] = d[key] + '#'

# print(d)

##############
###while
#################
# 
# spisok = [10, 40, 20, 30]
# i = 0
# while i < len(spisok):
#     spisok[i] = spisok[i] + 2  
#     i = i + 1
# print(spisok)

# ##############################
# # continue виходить з ітерації, починає наступну
# ################################################

# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i * 2, end='')

###############################
#break достроково перериває цикл
#####################################

# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i * 2, end='')
    
    #Службове слово else, яке застосовується 
    # в циклі while чи for перевіряє чи був вихід 
    # з циклу з допомогою слова break, блок коду
    # після else буде виконаний лише у випадку 
    # якщо не спрацював break
    ############################### 
# for i in 'hello world':
#     if i == 'a':
#         break
# else:
#     print('The letter is missing from the line')
# print("OOps!!!")

#############################
#range
##############################
# a = range(-10, 10)
# print(type(a))
# print(a)
# print(list(a))
####################

# spisok = [10, 40, 20, 30]
# print(list(range(len(spisok))))
# print(range(len(spisok)))

#############################################
#range(0, 4) генерує послідовність від 0 до 3
#############################################

# spisok = [10, 40, 20, 30]
# for i in range(len(spisok)):
#     spisok[i] += 2
#     print(i,spisok[i])



# name = ''
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')



# print('My name is')
# for i in range(5):
#     print('Anakin Skywalker (' + str(i) + ')')


# print('My name is')
# i = 0
# while i < 5:
#     print('Anakin Skywalker (' + str(i) + ')')
#     i += 1 # i += 1


# professions = {'business': 'economist', 'tv': 'newsreader', 'it': 'web developer', 'education': 'teacher'}
# for value in professions.values():
#     print(value)


# cars = ['BMW', 'Audi', 'Ford', 'Toyota']
# for i in cars:
#     print(i)

# professions = {'business': 'economist', 'tv': 'newsreader', 'it': 'web developer', 'education': 'teacher'}
# for key, value in professions.items():
#     print('Category', key, 'has a profession', value)


# drivers = {'Anton': 'Audi', 'Ivan': 'BMW', 'Pavlo': 'Toyota', 'Niko': 'Ford'}
# for name in sorted(drivers.keys()):
#     print(name.title() + ", thank you for taking the")


# popular_sites = ['Google.com', 'Youtube.com', 'Facebook.com', 'Baidu.com', 'Wikipedia.org', 'Yahoo.com' ,'Amazon.com']
# for i in range(len(popular_sites)):
#     print(i, popular_sites[i])


# popular_sites = ['Google.com', 'Youtube.com', 'Facebook.com', 'Baidu.com', 'Wikipedia.org', 'Yahoo.com' ,'Amazon.com']
# for index, value in enumerate(popular_sites, 1):
#     print(index, value)


# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['coconut', 'lemon', 'mango']
# drinks = ['coffee', 'tea', 'fruit juice']
# desserts = ['marmalade', 'ice cream', 'pie', 'pudding']
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)


# start = 0
# finish = 10
# while start<finish:
#     print(start)
#     start+=1
# else:
#     print("The end")    


def mean(n):
    digits = [int(d) for d in str(n)]
    return sum(digits) // len(digits)  