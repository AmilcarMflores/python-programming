grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]
list(zip(avgs, grades)) # [(22, 18), (21, 23), (29, 30), (24, 27)]

# Equivalente a zip
list(map(lambda *a: a, avgs, grades)) # [(22, 18), (21, 23), (29, 30), (24, 27)]