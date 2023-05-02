#1
def my_gen():
    value = range(10)
    for i in value:
        yield i
        print(next(value))
print(my_gen())


#2
for i in range(10):
    print (i) 