import sys

# По умолчанию глубина рекурсии составляет 1000 вызовов
print(sys.getrecursionlimit())
# 1000

# Делает возможным более глубокое вложение
sys.setrecursionlimit(10_000)

help(sys.setrecursionlimit)
