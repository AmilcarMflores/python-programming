# primes = []
# upto = 100
# for n in range(2, upto + 1):
#   is_prime = True
#   for divisor in range(2, n):
#     if n % divisor == 0:
#       is_prime = False
#       break
#   if is_prime:
#     primes.append(n)
# print(primes) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Forma un poco mejor
primes = []
upto = 100
for n in range(2, upto + 1):
  for divisor in range(2, n):
    if n % divisor == 0:
      break
  else:
    primes.append(n)
print(primes)