from decimal import Decimal as D
# Explicación del código

# Decimal es una clase que nos permite trabajar con números decimales
print(D(3.14))  # 3.140000000000000124344978758017532527446746826171875

# Podemos crear un número decimal a partir de una cadena
print(D("3.14"))  # 3.14

# Podemos realizar operaciones aritméticas con números decimales
print(D("0.1") * D(3) - D("0.3"))  # 0.0

# Podemos convertir un número decimal a una fracción
print(D("1.4").as_integer_ratio())  # (7, 5)