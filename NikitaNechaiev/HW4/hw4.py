temperature = int(input('Enter a celsius degree :'))
fahrenheit = (temperature * 9/5) + 32
if temperature > -273.15:
    print(f'{fahrenheit} - temperature in fahrenheit degree.')
elif temperature < -273.15:
    print(f'{temperature} - temperature below ablosute zero.')
  
