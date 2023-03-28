with open("E:\PycharmProjects\Softserve\Lv-14.03.PythonFundamentals\Zen.txt", "r") as file:
    philosophy = file.read().upper()

print(
f"""{philosophy}\n
better: {philosophy.count("BETTER")}
never:{philosophy.count("NEVER")}
is: {philosophy.count("IS")}"""
)