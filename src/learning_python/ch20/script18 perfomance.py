# Пространство памяти и время, лаконичность, выразительность
import math
print(math.factorial(10))   # 3628800

from src.learning_python.permute import permute1, permute2
seq = list(range(10))
p1 = permute1(seq)  # 6 секунд на компьютере с CPU Intel i9-13900K. 5.8 ГГц турбо режим
print(len(p1), p1[0], p1[1])

p2 = permute2(seq)  # Генератор немедленно возвращает управление
print(next(p2))     # И быстро производит каждый результат по запросу
print(next(p2))

p2 = list(permute2(seq)) # 5 секунд
print(p1 == p2)     # True
