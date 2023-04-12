# -------------------------------------------------------
# 1 TASK
def biggest_number(num1, num2):
    """
    So, this particular program just returns the biggest value.
    So, weather it is num1 or num2
    """
    if num1 > num2:
        print("{} is bigger".format(num1))
    elif num1 < num2:
        print("{} is bigger".format(num2))
    else:
        print(f"{num1} and {num2} are equal")


print(biggest_number(num2 = 25,num1 =24), biggest_number.__doc__)

# -------------------------------------------------------
# 2 TASK
desire = input("choose your figure: ").lower()

def rectangle():
    a = int(input("One side: "))
    b = int(input("The other side: "))
    square = a * b
    print(square)
    return square

def triangle():
    a = int(input("The basis: "))
    h = int(input("The height: "))
    square = (1/2) * a * h
    print(square)
    return square

def circle():
    r = int(input("The radius: "))
    square = float(3.14 * (r ** 2))
    print(square)
    return square

if desire == "rectangle":
    rectangle()

elif desire == "triangle":
    triangle()

elif desire == "circle":
    circle()

else:
    print("error")
# -------------------------------------------------------
# 3 TASK
# #
word = input("Enter a word: ")
def calculator():
    global word
    finish = {}
    for i in word:
        counter = word.count(i)
        if i in finish:
            continue
        else:
            put_into_list = finish.update({ str(i): counter})
    print(finish)
    return finish


calculator()