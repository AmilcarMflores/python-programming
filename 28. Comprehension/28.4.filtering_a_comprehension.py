# pythagorean.triple
# from math import sqrt

# # Esto generará todos los pares posibles
# mx = 10
# triples = [
#   (a, b, sqrt(a**2 + b**2))
#   for a in range(1, mx)
#   for b in range(a, mx)
# ]
# # Esto filtrará todos los triples no pitagóricos
# triples = list(
#   filter(lambda triple: triple[2].is_integer(), triples)
# )
# print(triples) # [(3, 4, 5.0), (6, 8, 10.0)]

# Usando comprensiones
from math import sqrt

mx = 10

# generar y filtrar en una sola comprensión
triples = [
  (a, b, int(c))
  for a in range(1, mx)
  for b in range(a, mx)
  if (c := sqrt(a**2 + b**2)).is_integer()
]
print(triples) # [(3, 4, 5), (6, 8, 10)]  