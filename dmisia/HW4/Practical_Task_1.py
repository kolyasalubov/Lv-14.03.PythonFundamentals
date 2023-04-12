temp1 = int(input('Enter the temperature in Celsius: '))
temp2 = int((temp1 * 9/5) + 32)
sign = chr(176)
if temp1 > -273.15:
    print(f"{temp1}{sign}C is equivalent to {temp2}{sign}F")
else:
    print(f"Error: Temperature below absolute zero (-273.15){sign}C")