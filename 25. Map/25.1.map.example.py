# 1 iterable
list(map(lambda *a: a, range(3))) # [(0,), (1,), (2,)]

# 2 iterables
list(map(lambda *a: a, range(3), "abc")) # [(0, 'a'), (1, 'b'), (2, 'c')]

# 3 iterables
list(map(lambda *a: a, range(3), "abc", range(4, 7))) # [(0, 'a', 4), (1, 'b', 5), (2, 'c', 6)]

# map se detiene cuando la iteración más corta se agota
list(map(lambda *a: a, (1, 2), "abc")) # [(1, 'a'), (2, 'b')]

list(map(lambda *a: a, (1, 2, 3, 4), "abc")) # [(1, 'a'), (2, 'b')]