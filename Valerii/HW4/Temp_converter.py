celsius = int(input('Enter temperature in Celsius: '))

if not celsius < -273.15:
    farenheit = (celsius * 9 / 5) + 32
    print(f'{celsius}°C is equivalent to {farenheit}°F')
else:
    print('Error: Temperature below absolute zero (-273,15°C)')
