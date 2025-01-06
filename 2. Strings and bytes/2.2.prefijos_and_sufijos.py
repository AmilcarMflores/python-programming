s = "Hello There"

# Prefijos
print(s.removeprefix("Hell")) # o There
# Sufijos
print(s.removesuffix("There")) # Hello T
# Si la cadena no tiene el prefijo o sufijo especificado, la cadena original se devuelve sin cambios
print(s.removeprefix("Ooops")) # Hello There