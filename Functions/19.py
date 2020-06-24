from functools import reduce
lists = [0,1]
  
fibonacci = lambda n: reduce(lambda x, n: x+[x[-1]+x[-2]], range(n-2), lists) 
  
print(fibonacci(10)) 