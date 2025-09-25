# Генераторные функции или генераторные выражения

G = (c * 4 for c in 'SPAM')     # Генераторное выражение
print(list(G))  # Заставляет генератор выпустить все результаты
# ['SSSS', 'PPPP', 'AAAA', 'MMMM']

def timesfour(S):   # Генераторная функция
    for c in S:
        yield c * 4
G = timesfour('spam')
print(list(G))
# ['ssss', 'pppp', 'aaaa', 'mmmm']

# Итерация вручную (выражение)
G = (c * 4 for c in 'SPAM')
I = iter(G)
print(next(I))  # SSSS
print(next(I))  # PPPP

# Итерация вручную (функция)
G = timesfour('spam')
I = iter(G)
print(next(I))  # ssss
print(next(I))  # pppp
