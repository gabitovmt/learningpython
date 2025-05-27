# Дробный тип

from fractions import Fraction

x = Fraction(1, 3)  # Числитель, знаменатель
y = Fraction(4, 6)  # Упрощается до 2, 3 по наибольшему общему делителю
print(repr(x))  # Fraction(1, 3)
print(repr(y))  # Fraction(2, 3)
print(y)  # 2/3
print('-' * 10 + '\n')

print(x + y)  # 1
print(x - y)  # -1/3
print(x * y)  # 2/9

print(repr(Fraction('.25')))  # Fraction(1, 4)
print(repr(Fraction('1.25')))  # Fraction(5, 4)
print(repr(Fraction('.25') + Fraction('1.25')))  # Fraction(3, 2)
print('-' * 10 + '\n')

print('Числовая точность дробных и десятичных типов')
a = 1 / 3.0  # Результат точен лишь настолько, насколько позволяют аппаратные средства
b = 4 / 6.0  # Точность может теряться из-за множества вычислений
print(a)  # 0.3333333333333333
print(b)  # 0.6666666666666666
print(a + b)  # 1.0
print(a - b)  # -0.3333333333333333
print(a * b)  # 0.2222222222222222

print(0.1 + 0.1 + 0.1 - 0.3)  # Должен быть нулём (близко, но не точно)
# 5.551115123125783e-17
print(repr(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)))
# Fraction(0, 1)
print('-' * 10 + '\n')

import decimal
from decimal import Decimal

print('Числовая точность, два пути')
print(1 / 3)
# 0.3333333333333333
print(Fraction(1, 3))
# 1/3
decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))
# 0.33
