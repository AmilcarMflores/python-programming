def func(a, b, c):
  print(a, b, c)
values = {"b": 1, "c": 2, "a": 42}
func(**values)  # 42 1 2