# Objeto bytearray vacío
bytearray() # bytearray(b'')

# Instacia llena de ceros con una longitud de determinada
bytearray(10) # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# byterray iterable de números enteros
bytearray(range(5)) # bytearray(b'\x00\x01\x02\x03\x04')

# Un bytearrat de bytes
name = bytearray(b"Lina") 
print(name)
print(name.replace(b"L", b"l"))

# .endswith() -> Devuelve True si el bytearray termina con el sufijo especificado
print(name.endswith(b'na')) # True

print(name.upper()) # bytearray(b'LINA')

print(name.count(b'L')) # 1