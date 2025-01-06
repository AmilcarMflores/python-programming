a = [1, 3, 5, 7]

# El valor mínimo de la lista
print(min(a)) # 1

# El valor máximo de la lista
print(max(a)) # 7

# La suma de los elementos de la lista
print(sum(a)) # 16

from math import prod
prod(a) # 105

# La longitud de la lista
print(len(a)) # 4

# Sobrecarga de operadores
b = [6, 7, 8]
a + b # [1, 3, 5, 7, 6, 7, 8]
a * 2 # [1, 3, 5, 7, 1, 3, 5, 7]