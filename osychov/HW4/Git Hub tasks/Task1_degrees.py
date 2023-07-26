def celcius_to_fahrenheit(temp_celcius):
    if temp_celcius < -273.15 :
        return "Temperature below absolute zero(-273.15°C)"
    fahrenheit = int((temp_celcius * 9/5) + 32)
    return fahrenheit
    
    
temp_celcius = int(input("Enter the temperature in Celsius: "))
print(f"{temp_celcius}°C is equivalent to {celcius_to_fahrenheit(temp_celcius)}°F")

