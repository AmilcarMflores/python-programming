# Conjunto vacío
small_primes = set()

small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes) # {2, 3, 5}

# 1 no es primo
small_primes.add(1)
print(small_primes) # {1, 2, 3, 5}

# 1 no es primo, así que lo eliminamos
small_primes.remove(1)

3 in small_primes # True
4 in small_primes # False
4 not in small_primes # True

# Intentando añadir de nuevo el 3
small_primes.add(3) # No hace nada
print(small_primes) # {2, 3, 5}

# Creación rápida de un conjunto
bigger_primes = set([5, 7, 11, 13])

# Unión con el operador |
small_primes | bigger_primes # {2, 3, 5, 7, 11, 13}

# Intersección con el operador &
small_primes & bigger_primes # {5}

# Diferencia con el operador -
small_primes - bigger_primes # {2, 3}

# Otra forma de crear un conjunto usando llaves
small_primes = {2, 3, 5, 5, 7}
print(small_primes) # {2, 3, 5, 7}
