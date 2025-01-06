t = ()
print(type(t))  # <class 'tuple'> 

one_element_tuple = (1, ) # (1,)
three_elements_tuple = (1, 3, 5) # (1, 3, 5)

3 in three_elements_tuple # True


# Si tenemos:
# Tupla explícita
t = (1, 2, 3)
# Desempaquetado de tupla
a, b, c = t # a = 1, b = 2, c = 3
type(t) # <class 'tuple'>
type(a) # <class 'int'>

# También podemos hacer esto:
a, b = 0, 1
a, b = b, a
print(a, b) # 1 0