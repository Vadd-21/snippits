def fib_gen(num):
  i1, i2 = 0, 1
  for i in range(num+1):
    yield i1
    i1, i2 = i2, i1 + i2
    
def fib_recurse(num, res=(0,1)):
  if num:
    return fib_recurse(num-1, (res[1], res[0] + res[1]))
  return res[0]
  
def main():
  x = fib_gen(6)
  for i in x:
    print(i)
  print(fib_recurse(6))
  lfib = lambda num : num if num < 2 else lfib(num-1) + lfib(num-2)
  print lfib(6)

if __name__ == "__main__":
  main()
