def factorial(n):
  if n in (0, 1): # Caso base
    return 1
  return factorial(n - 1) * n # Caso recursivo
    