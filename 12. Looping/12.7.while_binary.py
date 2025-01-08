# Convertir un número a binario con while
n = 39
remainders = []
while n > 0:
  remainder = n % 2
  remainders.append(remainder)
  n //= 2
remainders.reverse()
print(remainders)

# Otra forma de hacerlo:
n = 39
remainders = []
while n > 0:
  n, remainder = divmod(n, 2)
  remainders.append(remainder)
remainders.reverse()
print(remainders) # Output: [1, 0, 0, 1, 1, 1]