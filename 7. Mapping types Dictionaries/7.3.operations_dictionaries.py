d = {}

# Establezcamos un par de pares (clave, valor)
d["a"] = 1
d["b"] = 2

# ¿Cuántos pares (clave, valor) hay en el diccionario?
len(d)  # 2

# ¿Cuál es el valor de a?
d["a"] # 1

# ¿Cómo se ve d ahora?
d # {'a': 1, 'b': 2}

# Eliminemos a
del d["a"]
d # {'b': 2}

d["c"] = 3
# ¿c está en d?
"c" in d # True

# Valores que no están en d
3 in d # False
"e" in d # False

# Dejamos d vacío
d.clear()
d # {}