



#𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2
def fibonacci(num):
     a,b = 0,1
     while a < num:
          a,b = b, a+b
          print(a, end=' ')
     print(' - end.')
     

print(fibonacci(100))
          










