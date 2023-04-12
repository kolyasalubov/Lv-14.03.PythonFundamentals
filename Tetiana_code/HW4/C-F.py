C = float(input('Enter your temperature in Celsius '))
F = (C * float(9/5)) + 32
if C <= -273.15:
    print ('Error: Temperature below absolute zero')
else:
    print ('%0.1f C is equivalent to %0.1f F' %(C, F))