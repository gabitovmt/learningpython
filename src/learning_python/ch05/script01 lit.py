# Целые числа
print(1234, -24, 0, 9999999999)  # 1234 -24 0 9999999999

# Числа с плавающей точкой
print(1.23, 1., 3.14e-10, 4E210, 4.0e+210)  # 1.23 1.0 3.14e-10 4e+210 4e+210

# 16-е, 8-е, 2-е
print(0x9ff, 0X9ff, 0o177, 0O177, 0b101011, 0B101011)  # 2559 2559 127 127 43 43

# hex, oct, bin, int
print(hex(155), oct(155), bin(155))  # 0x9b 0o233 0b10011011
print(int('0x9b', 16), int('0o233', 8), int('0b10011011', 2))

# Комплексные числа
print(3 + 4j, 3.0 + 4.0j, 3J)  # (3+4j) (3+4j) 3j

# Множества
print(set('spam'), {1, 2, 3, 4})

# Типы расширений десятичных и дробных чисел
from decimal import Decimal
from fractions import Fraction

print(Decimal('1.0'), Fraction(1, 3))  # 1.0 1/3

# Булевский тип и константы
print(bool(1), bool(0), True, False)  # True False True False
