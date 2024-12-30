from fractions import Fraction

print(Fraction(10, 6))  # 5/3
print(Fraction(1, 3) + Fraction(2, 3)) # 1

f = Fraction(3, 5)
print(f.numerator)  # 3
print(f.denominator)  # 5

# f.as_integer_ratio() retorna una tupla con el numerador y el denominador
print(f.as_integer_ratio())  # (3, 5)

print(Fraction(0.125))  # 1/8

# Fraction("3 / 7") es una cadena que representa una fracción
print(Fraction("3 / 7")) # 3/7
 
print(Fraction("-.125"))  # -1/8
