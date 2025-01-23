# Lista de cubos
cubes = [x**3 for x in range(10)]

# Con filter()
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
print(list(odd_cubes1)) # [1, 27, 125, 343, 729] 

# Con expresión generadora
odd_cubes2 = (cube for cube in cubes if cube % 2)
print(list(odd_cubes2)) # [1, 27, 125, 343, 729]
