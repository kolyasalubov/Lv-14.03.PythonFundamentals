with open("E:\PycharmProjects\Softserve\Lv-14.03.PythonFundamentals\Zen.txt", "r") as file:
    philosophy = file.read()
    better = philosophy.count("better")
    never = philosophy.count("never")
    iss = philosophy.count("is")
    philosophy.replace("i", "&")

print(
f"""{philosophy.upper()}\n
better: {better}
never: {never}
is: {iss}
"""
)