# Обработка произвольных структур
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x            # Сложение чисел напрямую
        else:
            tot += sumtree(x)   # Рекурсия для подсписков
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L)) # 36

# Патологические случаи
print(sumtree([1, [2, [3, [4, [5]]]]]))
# 15
print(sumtree([[[[[1], 2], 3], 4], 5]))
# 15


# Рекурсия или очереди и стеки
def sumtree(L):         # Явная очередь с обходом в ширину
    tot = 0
    items = list(L)     # Начать с копии верхнего уровня
    while items:
        front = items.pop(0)    # Извлечь/удалить элемент в начале
        if not isinstance(front, list):
            tot += front        # Напрямую суммировать числа
        else:
            items.extend(front) # <== Добавить всё из вложенного подсписка
    return tot

print(sumtree(L)) # 36

def sumtree(L):         # Явный стек с обходом в глубину
    tot = 0
    items = list(L)     # Начать с копии верхнего уровня
    while items:
        front = items.pop(0)    # Извлечь/удалить элемент в начале
        if not isinstance(front, list):
            tot += front        # Напрямую суммировать числа
        else:
            items[:0] = front   # <== Присоединить спереди всё из вложенного подсписка
    return tot

print(sumtree(L)) # 36
