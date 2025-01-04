d = dict(zip("hello", range(5)))
print(d)

# Eliminando un elemento
d.popitem()
d # {'h': 0, 'e': 1, 'l': 3}

# Eliminando un elemento con la clave l
d.pop("l")
d # {'h': 0, 'e': 1}

# Actualizando un diccionario
d.update({"another": "value"})
d.update(a=13)
d # {'h': 0, 'e': 1, 'another': 'value', 'a': 13}

# Obteniendo un valor por clave
d.get("a") # 13

# Si no obtengo un valor por defecto me muestre:
d.get("b", 177) # 177

# Si b no existe
d.get("b") # None