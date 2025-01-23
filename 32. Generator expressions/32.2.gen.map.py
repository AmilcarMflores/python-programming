def adder(*n):
  return sum(n)

# Con map()
s1 = sum(map(adder, range(100), range(1, 101)))
print(s1) # 10000

# Con expresión generadora
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print(s2) # 10000