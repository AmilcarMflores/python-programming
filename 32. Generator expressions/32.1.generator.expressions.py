# Lista por comprensión
cubes = [k**3 for k in range(10)]
print(cubes) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Expresión generadora
cubes_gen = (k**3 for k in range(10))
print(cubes_gen) # <generator object <genexpr> at 0x7f8b1c1b3d60>
print(list(cubes_gen)) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]