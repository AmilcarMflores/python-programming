def counter(start=0):
  n = start
  while True:
    yield n
    n += 1

c = counter()
print(next(c)) # 0
print(next(c)) # 1
print(next(c)) # 2