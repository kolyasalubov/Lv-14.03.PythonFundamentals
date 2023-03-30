celsius = float(input("Enter the temperature in Celsius: "))
if celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    print(f"{celsius}°C is equal to {(celsius * 9 / 5) + 32}°F")