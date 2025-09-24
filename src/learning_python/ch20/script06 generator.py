# Генераторные функции в действии

def gensquares(N):
    for i in range(N):
        yield i ** 2    # Позже возобновить здесь выполнение

for i in gensquares(5):     # Возобновление выполнения функции
    print(i, end=' : ')     # Вывод последнего выданного значения
print()
# 0 : 1 : 4 : 9 : 16 :

x = gensquares(4)
print(x)
# <generator object gensquares at 0x000002AB20CAB2A0>

print(next(x)) # 0
print(next(x)) # 1
print(next(x)) # 4
print(next(x)) # 9
try:
    next(x)
except StopIteration:
    print('StopIteration')

y = gensquares(5)   # Возвращает генератор, который сам по себе является итератором
print(iter(y) is y) # iter() не требуется: здесь ничего не делает
print(next(y))      # Можно запускать next() непосредственно
