from itertools import count
for n in count(5, 3):
  if n > 20:
    break
  print(n, end=", ") # 5, 8, 11, 14, 17, 20,