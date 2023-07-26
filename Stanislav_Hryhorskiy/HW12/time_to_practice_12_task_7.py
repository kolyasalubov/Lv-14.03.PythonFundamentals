# *** Task 7 ***
# Using several decorators, create a sandwich consisting of
# lettuce, tomatoes and meat.
# <\ ^^^^^^^ />
# # tomato #
# – meat–
# ~ salad ~
# <\ ______ />

def get_bottom_top_sandwich(func):
    def inner(*args, **kwargs):
        print("</ ^^^^^^^^ \>")
        func(*args, **kwargs)
        print("<\ ________ />")
    return inner


def get_tomato_salad(func):
    def inner(*args, **kwargs):
        print("  # tomato #")
        func(*args, **kwargs)
        print("  ~ salad ~")
    return inner


@ get_bottom_top_sandwich
@ get_tomato_salad
def get_sandwich(base):
    print(f"  - {base} -")


print("This sandwich is so yummy:")
get_sandwich("meat")
