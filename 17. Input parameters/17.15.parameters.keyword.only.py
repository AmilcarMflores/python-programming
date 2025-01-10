def kwo(*args, c):
  print(args, c)
kwo(1, 2, 3, c=7) # (1, 2, 3) 7
kwo(c=4) # () 4
kwo(1, 2) # (1, 2) Error
