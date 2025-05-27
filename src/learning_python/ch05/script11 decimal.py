# Основы десятичных чисел

print(0.1 + 0.1 + 0.1 - 0.3)
# 5.551115123125783e-17: недостаточно битов, чтобы обеспечить точность

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
# 0.0

# Python автоматически выполняет преобразование точности к наибольшему кол-ву десятичных цифр после точки
print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))
# 0.00

# float -> Decimal
print(Decimal.from_float(1.25)) # Python 2.7 и 3.1+
print(Decimal(1.25)) # В последних версиях Python
print('-' * 10)

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
# 2.775557561565156540423631668E-17

print(Decimal(1) / Decimal(7))
# 0.1428571428571428571428571429

import decimal
# В пакете decimal можно указывать точность и режимы округления для новых объектов Decimal в вызывающем потоке

decimal.getcontext().prec = 4
print(Decimal(1) / Decimal(7))
# 0.1429

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
# 1.110E-17

print('\nДиспетчер контекста для десятичных чисел')
print(Decimal('1.00') / Decimal('3.00'))  # 0.3333
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(Decimal('1.00') / Decimal('3.00'))  # 0.33
print(Decimal('1.00') / Decimal('3.00'))  # 0.3333
