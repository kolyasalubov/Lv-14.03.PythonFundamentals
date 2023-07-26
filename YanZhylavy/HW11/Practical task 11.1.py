def age_processor(age):
  if int(age) < 0:
    raise ValueError ('Age cannot be negative')

  elif int(age)%2 == 0:
    return 'Your age is even'

  else:
    return'Your age is odd'

age = input('Enter your age: ')

print(age_processor(age))