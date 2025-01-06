from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]

# Ordenar la lista por el primer elemento de cada tupla
sorted(a) # [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]


sorted(a, key=itemgetter(0)) # [(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]

sorted(a, key=itemgetter(0, 1)) # [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]

sorted(a, key=itemgetter(1)) # [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]

sorted(a, key=itemgetter(1), reverse=True) # [(4, 9), (1, 3), (5, 3), (1, 2), (2, -1)]