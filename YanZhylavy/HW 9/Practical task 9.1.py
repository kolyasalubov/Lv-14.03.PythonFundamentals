import random

number = random.randint(1,40)

counter = 10

while True:
  guess_number = int(input (f'I made up a number, can you guess it? You have {counter} attempts \U0001f642  - '))
  if guess_number == number:
    print("You are the winner \U0001f44f")
    break
  elif 1<=guess_number<=40 and guess_number < number:
     print("Your number is less, try again \U0001f641")
  
  elif 1<=guess_number<=40 and guess_number > number:
     print("Your number is more, try again \U0001f641")

  elif not 1<=guess_number<=10:
     print("Your number is out of range \U0001f624")
  counter = counter - 1
  if counter < 1:
    print("Sowwy, your attempts are over \U0001f62d")
    break