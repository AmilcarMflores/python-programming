def minimum(*n):
  # print(type(n)) # <class 'tuple'>
  if n:
    mn = min(n)
    print(mn)
    
minimum(1, 3, -7, 9) # -7
minimum() # None