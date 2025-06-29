# Оператор pass
# Ещё один бесконечный цикл
# while True: pass

def func():
    pass  # Позже поместить сюда реальный код


def func2():
    ...  # Альтернатива pass


X = ...  # Альтернатива None
print(repr(X))

# Оператор continue
x = 10
while x:
    x -= 1
    if x % 2 != 0: continue  # Нечётное? Тогда пропустить print
    print(x, end=' ')
print()
# 8 6 4 2 0

# Более ясный вариант
x = 10
while x:
    x -= 1
    if x % 2 == 0:  # Чётное? Тогда вывести
        print(x, end=' ')
print()
# 8 6 4 2 0
