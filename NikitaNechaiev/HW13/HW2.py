def up_of_sandw(func):
    def inner(*args, **kwargs):
        print('</','^'*10,'/>')
        func(*args, **kwargs)
        print('</','_'*10,'/>')
    return inner


def middle_of_sandw(func):
    def inner(*args, **kwargs):
        print('#tomato#\n-meat-\n~salad~')
    return inner
    

@up_of_sandw
@middle_of_sandw
def printer(buter):
    print(buter)
printer("Hello")
