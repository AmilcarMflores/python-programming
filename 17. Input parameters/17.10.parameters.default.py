def func(a, b=4, c=88):
  print(a, b, c)
func(1) # 1 4 88
func(b=5, a=7, c=9) # 7 5 9
func(42, c=9) # 42 4 9
func(42, 43, 44) # 42 43 44