def fib(n):
      a,b=0,1
      for i in range(n+1):
          yield a
          a,b=b,a+b
if __name__=="__main__":
    num=10
    for x in fib(num):
        print(x, end=',')

