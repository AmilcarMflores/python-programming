number = 4
exponent = 2

# Modular Exponentiation
mod_exp = pow(number, exponent, 16)

print(mod_exp)  # 16

# Otra forma de hacer exponente modular
mod_exp_2 = (number ** exponent) % 16

# Modular inverse
mod_inv = pow(37, -1, 43)

print(mod_inv)  # 7

