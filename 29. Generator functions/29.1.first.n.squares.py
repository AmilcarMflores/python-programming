# Función clásica
def get_squares(n):
  return [x**2 for x in range(n)]
print(get_squares(10)) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Función generadora
def get_squares_gen(n):
  for x in range(n):
    yield x**2
print(list(get_squares_gen(10))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]