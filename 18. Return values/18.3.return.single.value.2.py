from functools import reduce
from operator import mul
def factorial(n):
  return reduce(mul, range(1, n + 1), 1)
f5 = factorial(5) # f5 is 120