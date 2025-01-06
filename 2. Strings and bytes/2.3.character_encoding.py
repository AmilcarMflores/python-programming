s = "This is üŋíc0de"
print(type(s)) # <class 'str'>

# Codificación de caracteres a bytes
encoded_s = s.encode("utf-8")
print(encoded_s) # b'This is \xc3\xbc\xc5\x8b\xc3adc0de'
print(type(encoded_s)) # <class 'bytes'>

# Decodificación de bytes a caracteres
decoded_s = encoded_s.decode("utf-8")
print(decoded_s) # This is üŋíc0de

# Crear un objeto de bytes
bytes_obj = b"A bytes object"
print(type(bytes_obj)) # <class 'bytes'>