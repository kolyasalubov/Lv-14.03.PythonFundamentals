cel = int(input("Enter your temperature in Celsius: "))
if cel > -273.15:
    fahr = (cel*9/5)+32
    print(f"Your temparature in Celsius: {cel}° C\n"
          f"Your temperature in Fahrenheit: {fahr}° F")
else:
    print("Error! Your temperature below absolute zero!")