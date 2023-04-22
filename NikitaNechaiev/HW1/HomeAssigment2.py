# Спочатку робив по гайду з ютуба а потім второпав і зрозумів як писати.
# Не зрозумів як ** можно втиснути в код.
#Додавання 
#Віднімання
#Множення
#Ділення
operator = input("Оберіть дію (+ - * / % //): ")
num1 = float(input("Вкажіть перше число: "))
num2 = float(input("Вкажіть друге число: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
elif operator == "%":
    result = num1 % num2
    print(result)
elif operator == "//":
    result = num1 //num2
    print(result)
