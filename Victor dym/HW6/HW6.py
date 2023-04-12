# ---------------------------------------------------------------------------
# 1 TASK

list_even = []
list_odd = []
list_else = []
for i in range(1, 11):
    if i % 2 == 0:
        list_even.append(i)
    elif i % 3 == 0:
        list_odd.append(i)
    else:
        list_else.append(i)

print("Here is the list of even numbers that are divisible by 2 ", list_even)
print("Here is the list of odd numbers that are divisible by 3: {}".format(list_odd))
print(f"Here is the list of all left numbers: {list_else}")

# ---------------------------------------------------------------------------
# 2 TASK

login = 0
login_try = "First"
def function_check():
    global login
    while login != login_try:
        login = input("Enter your login: ")
        if login == login_try:
            print("Nice, you passed ")
        else:
            print("Try again ")

function_check()