C = int(input("Enter the temperature in Celcius:"))

if C>-273:
    F = int((C*9/5) + 32)
    print(f"{C}\u00B0C is equivalent to {F}\u00B0F")
else:
    print("Error. Temperature below absolute zero (-273.15 C)")

