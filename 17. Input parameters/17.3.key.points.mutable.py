x = [1, 2, 3]
def func(x):
  x[1] = 42 # afecta al argumento x
func(x)
print(x) # [1, 42, 3]