N = 20

# Con map() y filter()
cubes1 = map(
  lambda n: (n, n**3),
  filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N)),
)

# Con expresión generadora
cubes2 = ((n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)

# Ambos producen el mismo resultado: [(0, 0), (3, 27), (5, 125), (6, 216), (9, 729), (10, 1000), (12, 1728), (15, 3375), (18, 5832)]