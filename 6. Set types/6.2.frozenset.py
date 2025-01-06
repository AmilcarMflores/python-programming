small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])

# No podemos usar .add ni .remove
# small_primes.add(11) # AttributeError
# small_primes.remove(2) # AttributeError

# Pero podemos hacer operaciones de conjuntos
print(small_primes & bigger_primes) # frozenset({5, 7})