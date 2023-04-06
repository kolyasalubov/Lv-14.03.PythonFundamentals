number = int(input("Enter your number: ")) # Get the number 
number_copy = number # Do copy of our number 

if number_copy >= 0: # Check our received number
    fact = 1 # By default, we set the parameter factorial to 1
    while number_copy != 0:
        fact *= number_copy 
        number_copy -= 1
    print(f"The factorial of a {number} is {fact}")
else:
    print(f"The factorial of your number {number} "
          "can't be determined. Most likely, it is less than 0!")
    