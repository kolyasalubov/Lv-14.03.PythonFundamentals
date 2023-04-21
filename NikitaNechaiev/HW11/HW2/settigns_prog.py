def checker():
   try:
      val = int(input("Enter your age: "))
      if val <= 0:
         raise ValueError('Value error!')
      elif val % 2 == 0:
         print('even')
      elif val % 2 == 1:
         print('Odd')
   except ValueError as e:
      print(e)
checker()