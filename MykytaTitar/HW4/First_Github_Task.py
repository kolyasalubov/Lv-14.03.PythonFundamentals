celsius = float(input("Enter the temperature in Celcius:"))

if celsius>-273.15:
    fahrenheit = int((C*9/5) + 32)
    print(f"{celsius}\u00B0C is equivalent to {fahrenheit}\u00B0F")
else:
    print("Error. Temperature below absolute zero (-273.15 C)")

