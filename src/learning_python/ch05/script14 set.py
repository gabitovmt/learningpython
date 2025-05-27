# Множества

x = set('abcde')
y = set('bdxyz')
print(x - y)  # Разность: {'a', 'e', 'c'}
print(x | y)  # Объединение: {'x', 'e', 'c', 'z', 'y', 'b', 'a', 'd'}
print(x & y)  # Пересечение: {'b', 'd'}
print(x ^ y)  # симметричная разность (исключающее ИЛИ): {'e', 'a', 'z', 'y', 'c', 'x'}
print(x > y, x < y)  # Надмножество, подмножество: False, False
print('-' * 10 + '\n')

print(x.difference(y))  # x - y
print(x.union(y))  # x | y
print(x.intersection(y))  # x & y
print(x.symmetric_difference(y))  # x ^ y
print(x.issuperset(y), x.issubset(y))  # x > y, x < y
print('-' * 10 + '\n')

z = x.intersection(y)  # x & y
print(z)  # {'d', 'b'}
z.add('SPAM')
print(z)  # {'SPAM', 'b', 'd'}
z.update({'x', 'y'})  # Слияние: объединение на месте
print(z)  # {'x', 'SPAM', 'y', 'd', 'b'}
z.remove('b')
print(z)  # {'SPAM', 'x', 'd', 'y'}
print('-' * 10 + '\n')

for item in set('abc'): print(item * 3)
# bbb
# aaa
# ccc

print('Методы множеств могут работать с любым итерируемым типом')
S = {1, 2, 3}
# S | [3, 4]    TypeError
print(S.union([3, 4]))  # {1, 2, 3, 4}
print(S.intersection((1, 3, 5)))  # {1, 3}
print(S.issubset(range(-5, 5)))  # True
