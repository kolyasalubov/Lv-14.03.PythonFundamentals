"""
*** Practical Task 1. "Temperature Converter" ***
Write a Python program that prompts the user to enter a temperature in Celsius and then
converts it to Fahrenheit using the formula: F = (C * 9/5) + 32. Your program should then
print out the converted temperature in Fahrenheit.
However, if the user enters a temperature below -273.15°C (the lowest possible
temperature in the universe, also known as absolute zero), your program should print an
error message instead of attempting to convert the temperature.
Note: You can assume that the user will enter a valid input
(a number for the temperature in Celsius).
Example output:
Enter the temperature in Celsius: 25
25°C is equivalent to 77°F
Example output (if the user enters a temperature below absolute zero):
Enter the temperature in Celsius: -300
Error: Temperature below absolute zero (-273.15°C)
"""

ABSOLUTE_ZERO = -273.15  # °C
temperature = float(input("Enter the temperature in Celsius (°C): "))

if temperature < ABSOLUTE_ZERO:
    print(f"Error: Temperature below absolute zero ({ABSOLUTE_ZERO} °C)")
else:
    Fahrenheit_temperature = 1.8 * temperature + 32
    Kelvin_temperature = temperature - ABSOLUTE_ZERO
    Rankine_temperature = 1.8 * temperature + 491.67
    Reaumur_temperature = 0.8 * temperature
    print(f"The temperature of {temperature} °C:\n"
          f"\t-on the Fahrenheit scale equivalent: {Fahrenheit_temperature:.2f} °F;\n"
          f"\t-on the Kelvin scale equivalent: {Kelvin_temperature:.2f} °K;\n"
          f"\t-on the Rankine scale equivalent: {Rankine_temperature:.2f} °Ra;\n"
          f"\t-on the Reaumur scale equivalent: {Reaumur_temperature:.2f} °Re."
          )
