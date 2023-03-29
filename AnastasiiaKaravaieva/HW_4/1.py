
c = int(input("Write your temperature in Celsius:"))

if c < -273.15:
    print("Error. You can't convert temperature below absolute zero(-273.15 C")
else:
    f = (c * 9/5) + 32
    print(f"{c} C is equivalent to {f} F ")

