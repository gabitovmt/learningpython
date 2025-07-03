# Ручная итерация: iter и next
f = open('text.txt', encoding='utf-8')
print(next(f), end='')
print(next(f), end='')

L = [1, 2, 3]
I = iter(L) # Получение объекта итератора из итерируемого объекта
print(I.__next__()) # Вызов метода next итератора для продвижения на следующий элемент
print(I.__next__())
print(I.__next__())
# print(I.__next__()) Исключение StopIteration

# Файловый объект является итератором сам по себе
f = open('text.txt', encoding='utf-8')
print(iter(f) is f)
# True
print(f.__iter__() is f)
# True

print(iter(L) is L)
# False

print('-' * 80)

L = [1, 2, 3]

for X in L: # Автоматическая итерация
    print(X ** 2, end=' ')
print()

I = iter(L) # Ручная итерация
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print(X ** 2, end=' ')
print()
