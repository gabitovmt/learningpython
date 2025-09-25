# Генераторы являются объектами с одиночной итерацией

G = (c * 4 for c in 'SPAM')
print(iter(G) is G) # Итератором генератора является сам генератор
# True

G = (c * 4 for c in 'SPAM') # Создать новый генератор
I1 = iter(G)    # Итерация вручную
print(next(I1)) # SSSS
print(next(I1)) # PPPP
I2 = iter(G)    # Второй генератор находится в той же самой позиции!
print(next(I2)) # AAAA

print(list(I1)) # Собирает оставшиеся элементы I1
# ['MMMM']
try:
    print(next(I2)) # Другие итераторы тоже израсходуются
except StopIteration:
    print('StopIteration')

try:
    I3 = iter(G)    # То же самое касается новых итераторов
    next(I3)
except StopIteration:
    print('StopIteration')

I3 = iter(c * 4 for c in 'SPAM')   # Новый генератор, чтобы начать заново
print(next(I3)) # SSSS


print('-' * 80)
def timesfour(S):
    for c in S:
        yield c * 4
G = timesfour('spam')   # Генераторные функции работают таким же образом
print(iter(G) is G)
# True
I1, I2 = iter(G), iter(G)
print(next(I1)) # ssss
print(next(I1)) # pppp
print(next(I2)) # aaaa


print('-' * 80)
L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)
print(next(I1)) # 1
print(next(I1)) # 2
# Списки поддерживают множество итераторов
print(next(I2)) # 1
# Изменения отражаются в итераторах
del L[2:]
try:
    print(next(I1))
except StopIteration:
    print('StopIteration')
