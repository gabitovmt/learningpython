# Числа
# Математика с плавающей точкой
print(1 / 3)
print((2 / 3) + (1 / 2))

# Десятичные числа: фиксированная точность
import decimal

d = decimal.Decimal('3.141')
print(d + 1)  # Decimal('4.141')
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))  # Decimal('0.33')

# Дроби: числитель + знаменатель
from fractions import Fraction

f = Fraction(2, 3)
print(f + 1)  # Fraction(5, 3)
print(f + Fraction(1, 2))  # Fraction(7, 6)
