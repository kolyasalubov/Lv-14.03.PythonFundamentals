c = int(input("Enter the temperature in Celsius: "))



if c > -273.15:
    Fahrenheit = (c * 9 / 5) + 32
    print(f"{c} is equivalent to {Fahrenheit}F")
else:
    print("Error: The temperature is below absolute zero (-273.15 C)")