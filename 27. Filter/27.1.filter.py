test = [2, 5, 8, 0, 0, 1, 0]

# Filtrar eliminando elementos falsos (None equivale a función identidad)
print(list(filter(None, test)))  # [2, 5, 8, 1]

# Equivalente al anterior con una función lambda
print(list(filter(lambda x: x, test)))  # [2, 5, 8, 1]

# Filtrar elementos mayores a 4
print(list(filter(lambda x: x > 4, test)))  # [5, 8]