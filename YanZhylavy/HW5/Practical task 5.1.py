elements = int(input('''Please, tell how many elements
from Fibonacci`s sequence you`d like to see: '''))
  
n1 = 0
n2 = 1

for i in range(elements):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
