# Суммирования с помощью рекурсии

def mysum(L):
    print(L) # Трассировка уровней рекурсии
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:]) # Рекурсивный вызов самой себя

print(mysum([1, 2, 3, 4, 5]))
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5]
# [3, 4, 5]
# [4, 5]
# [5]
# []
# 15
print('-' * 80)


# Альтернативные варианты кода

def mysum1(L):
    # Использование тернарного выражения
    return 0 if not L else L[0] + mysum1(L[1:])

def mysum2(L):
    # Любой тип, предполагая наличие хотя бы одного элемента
    return L[0] if len(L) == 1 else L[0] + mysum2(L[1:])

def mysum3(L):
    # Применение расширенного присваивания последовательностей Python 3.X
    first, *rest = L
    return first if not rest else first + mysum3(rest)


print(mysum1([1]))
print(mysum2([1]))
print(mysum3([1]))
# 1

print(mysum1([1, 2, 3, 4, 5]))
print(mysum2([1, 2, 3, 4, 5]))
print(mysum3([1, 2, 3, 4, 5]))
# 15

# print(mysum1(['s', 'p', 'a', 'm']))   TypeError
print(mysum2(['s', 'p', 'a', 'm']))
print(mysum3(['s', 'p', 'a', 'm']))
# spam

# print(mysum1(['spam', 'ham', 'eggs']))    TypeError
print(mysum2(['spam', 'ham', 'eggs']))
print(mysum3(['spam', 'ham', 'eggs']))
# spamhameggs

print(mysum1([]))
# print(mysum2([]))   IndexError
# print(mysum3([]))   ValueError
# 0
