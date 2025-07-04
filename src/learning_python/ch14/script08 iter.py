# Итераторы с множеством проходов или с одним проходом
R = range(3) # range допускает множество итераторов
# print(next(R))
# TypeError
I1 = iter(R)
print(next(I1))
# 0
print(next(I1))
# 1
I2 = iter(R) # Два итератора на одном диапазоне
print(next(I2))
# 0
print(next(I1))
# 2

Z = zip((1, 2, 3), (10, 11, 12))
I1 = iter(Z)
I2 = iter(Z) # Два итератора на одном результате zip
print(next(I1))
# (1, 10)
print(next(I1))
# (2, 11)
print(next(I2)) # I2 находится не в том же месте, что и I1!
# (3, 12)

M = map(abs, (-1, 0, 1)) # То же самое для результата map (и filter)
I1 = iter(M); I2 = iter(M)
print(next(I1), next(I1), next(I1))
# 1 0 1
# print(next(I2))
# StopIteration
