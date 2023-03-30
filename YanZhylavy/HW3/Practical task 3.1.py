celcius = input('Please enter the temperature value in Celsius to convert it to Fahrenheit: ')
fahrenheit = (float(celcius) * 9/5) + 32
if float(celcius)<-273.15:
    print('error:\nEntered temperature is below absolute zero')
else:
    print(fahrenheit)    