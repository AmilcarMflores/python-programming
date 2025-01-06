a = list("hello")
print(a) # ['h', 'e', 'l', 'l', 'o']

a.append(100)
print(a) # ['h', 'e', 'l', 'l', 'o', 100]

# Extender la lista usando una tupla
a.extend((1, 2, 3))
print(a)

# Extender usando una cadena
a.extend('...')
print(a) # ['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']