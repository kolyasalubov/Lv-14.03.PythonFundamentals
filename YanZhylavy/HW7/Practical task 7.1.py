def largest_num(num1:int,num2:int) ->int:
  """
  The function takes two numbers 
  and returns the largest of them.
  
  """
  try:
    if num1==num2:
      return 'Numbers are equel'
    elif num2>num1:
      return num2
    else:
      return num1
  except:
    return 'Error. Make sure you have entered two numbers.'



# Condition of the task said about only two numbers,
# but there is the same for more then two numbers, just in case :)
#                            |
#                            |
#                            |
#                            V



def largest_of_all(*args:int)->int:
  """
  The function returns the largest of all entered numbers.
  """
  try:
      answ = 0
      for i in args:
          if i> answ:
              answ = i
      return answ    
  except:
      return "Error. Make sure you have entered numbers."
  