# Преобразование дробей и разнородные типы

from fractions import Fraction

x = Fraction.from_float(2.5)
y = float(x)
print(repr(x))  # Fraction(5, 2)
print(repr(y))  # 2.5
print('-' * 10 + '\n')

z = 2.5.as_integer_ratio()  # Возвращает числитель и знаменатель
print(repr(z))  # (5, 2)

f = 2.5
a = Fraction(*f.as_integer_ratio())
# символ * - специальный синтаксис, который раскрывает кортеж в индивидуальные аргументы
print(repr(a))
print('-' * 10 + '\n')

print('Разрешено смешивать некоторые типы')
x = Fraction(1, 3)
print(repr(x + 2))  # дробь + целое = дробь: Fraction(7, 3)
print(repr(x + 2.0))  # дробь + с плавающей точкой = с плавающей точкой: 2.3333333333333335
print(repr(x + (1. / 3)))  # 0.6666666666666666

a = x + Fraction(*(4.0 / 3).as_integer_ratio())
print(repr(a))  # Fraction(22517998136852479, 13510798882111488) - точность теряется из-за числа с плавающей точкой
print(repr(a.limit_denominator(10)))  # Fraction(5, 3) - упростить до ближайшей дроби
