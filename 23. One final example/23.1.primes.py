from math import sqrt, ceil
def get_primes(n):
  """Calcular una lista de números primos hasta n (inclusive)."""
  primelist = []
  for candidate in range(2, n+1):
    is_prime = True
    root = ceil(sqrt(candidate))
    for prime in primelist:
      if prime > root:
        break
      if candidate % prime == 0:
        is_prime = False
        break
    if is_prime:
      primelist.append(candidate)
  return primelist

print(get_primes(100))