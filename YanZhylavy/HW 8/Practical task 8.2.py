password = input('Enter password: ')
list_of_boolians = []
digits = []
uppers = []
lowers = []
sym = []

symbols = ['#','@','$']

for i in password:
  if i.isdigit():
    digits.append(True)
  elif i.isupper():
    uppers.append(True)
  elif i.islower():
    lowers.append(True)
  elif i in symbols:
    sym.append(True)
  else:
    list_of_boolians.append(False)
if 6<=len(password)<=16:
  list_of_boolians.append(True)
else:
  list_of_boolians.append(False)
  
list_of_boolians.append(any(digits)) 
list_of_boolians.append(any(uppers))
list_of_boolians.append(any(lowers))
list_of_boolians.append(any(sym))

if all(list_of_boolians):
  print('Password is valid')
else:
  print('Password is invalid')