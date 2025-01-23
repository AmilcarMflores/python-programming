# Pares para bucle anidado
# items = "ABCD"
# pairs = []
# for a in range(len(items)):
#   for b in range(a, len(items)):
#     pairs.append((items[a], items[b]))
    
# Usando comprensiones
items = "ABCD"
pairs = [
  (items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))
]
print(pairs) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]