d = dict(zip("hello", range(5)))

# ¿Qué claves hay en d?
d.keys()  # dict_keys(['h', 'e', 'l', 'o'])

# ¿Qué valores hay en d?
d.values()  # dict_values([0, 1, 3, 4])

# ¿Qué pares (clave, valor) hay en d?
d.items()  # dict_items([('h', 0), ('e', 1), ('l', 3), ('o', 4])

3 in d.values()  # True

# ¿Está la clave "o" en d?
("o", 4) in d.items() # True


# setdefault() -> Si la clave no existe, la crea con el valor por defecto
e = {}
e.setdefault("a", 1)
e # {'a': 1}

# Intentamos anular el valor de "a"
e.setdefault("a", 2)
e # {'a': 1}

z = {}
z.setdefault("a", {}).setdefault("b", []).append(1)
z # {'a': {'b': [1]}}