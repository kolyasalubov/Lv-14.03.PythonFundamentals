week = {1:'Monday', 
    2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
day_number = input('Enter a number of the day in a week: ' )
if not day_number.isnumeric():
  raise ValueError ('There must be an integer')

elif int(day_number) >= 8:
  raise ValueError ('There are not so many days in a week')

else:
  print (week.get(int(day_number)))