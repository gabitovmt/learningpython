# Конструкция else цикла

def is_prime(y):
    x = y // 2  # Для значений y > 1
    while x > 1:
        if y % x == 0:  # Остаток от деления
            print(f'{y} has factor {x}')  # Имеет сомножитель
            break  # Пропуск else
        x -= 1
    else:  # Нормальный выход
        print(f'{y} is prime')  # Является простым


is_prime(3)
# 3 is prime
is_prime(10)
# 10 has factor 5

# Ещё пример. Поиск
def found1(x, search):
    found = False
    while x and not found:
        if x[0] == search:
            print('Ni')
            found = True
        else:
            x = x[1:]
    if not found:
        print('not found')


# Поиск с реализацией ветки else цикла
def found2(x, search):
    while x:
        if x[0] == search:
            print('Ni')
            break
        x = x[1:]
    else:
        print('not found')


X = [1, 2, 3]
found1(X, 2)
found2(X, 2)
# Ni
found1(X, 4)
found2(X, 4)
# not found
