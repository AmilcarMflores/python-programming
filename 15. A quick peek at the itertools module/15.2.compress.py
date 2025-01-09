# compress.py
from itertools import compress

data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))
print(odd_selector) # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
print(list(data)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_numbers) # [0, 2, 4, 6, 8]
print(odd_numbers) # [1, 3, 5, 7, 9]