celsius = float(input("Enter the temperature in Celsius: \n"))

if celsius <= -273.15:
  print("Error: Temperature below absolute zero (-273.15°C)")
  quit()
fahrengeit = ((celsius * 9) / 5) + 32
print(fahrengeit)