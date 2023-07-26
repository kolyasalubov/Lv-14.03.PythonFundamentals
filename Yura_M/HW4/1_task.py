enter = int(input("Enter the temperature in degrees Celsius: "))

if enter < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    F = (enter*9/5)+32
    print(f"{enter}°C is equivalent to {int(F)}°F")
