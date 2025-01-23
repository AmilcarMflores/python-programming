# No le asigna un valor a Alice
students = ["Sophie", "Alex", "Charlie", "Alice"]
grades = ["A", "C", "B"]
dict(zip(students, grades)) # {'Sophie': 'A', 'Alex': 'C', 'Charlie': 'B'}

# Para estos casos, tenemos que asegurarnos de que las listas tengan la misma longitud
dict(zip(students, grades, strict=True)) # ValueError: zip() argument after * must be an iterable, not bool
