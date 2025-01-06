a = [1, 2, 1, 3]

# Agregar un elemento al final de la lista
a.append(13)
print(a) # [1, 2, 1, 3, 13]

# Cuántos 1 hay en la lista
print(a.count(1)) # 2

# Extender la lista con otra lista
a.extend([5, 7])
print(a) # [1, 2, 1, 3, 13, 5, 7]

# Posición del 13 en la lista
print(a.index(13)) # 4

# Insertar el 17 a la posición 0
a.insert(0, 17)
print(a) # [17, 1, 2, 1, 3, 13, 5, 7]

# Eliminar el último elemento de la lista
a.pop() # 7

# Eliminar el elemento en la posición 3
a.pop(3) # 1

print(a) # [17, 1, 2, 3, 13, 5]

# Eliminar 17 de la lista
a.remove(17)

# Invertir el orden de la los elementos de la lista
print(a)
a.reverse()
print(a)

# Ordenar la lista
a.sort()
print(a)

# Elimitar todos los elementos de la lista
a.clear()
print(a) # []