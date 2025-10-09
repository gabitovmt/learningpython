# Упражнения части IV. Переменное количество аргументов

def adder(*args):
    if len(args) == 0:
        return None
    if len(args) == 1:
        return args[0]

    acc = args[0]
    for x in args[1:]:
        acc += x

    return acc


print(adder())
print(adder(1))
print(adder(1, 2))
print(adder(1, 2, 3))
print(adder(5.0, 10.0))
print(adder('a', 'b'))
print(adder([1], [2]))


def adder1(*args):
    print('adder1', end=' ')
    if type(args[0]) == type(0):  # Целое число?
        acc = 0
    else:
        acc = args[0][:0]  # Использовать пустой срез arg1
    for arg in args:
        acc = acc + arg
    return acc


# print(adder1())   не работает
print(adder1(1))
print(adder1(1, 2))
print(adder1(1, 2, 3))
# print(adder1(5.0, 10.0))  не работает
print(adder1('a', 'b'))
print(adder1([1], [2]))


def adder2(*args):
    print('adder2', end=' ')
    acc = args[0]   # Инициализировать первым аргументов
    for next in args[1:]:
        acc += next # Добавить элементы 2..N
    return acc


# print(adder2())   не работает
print(adder2(1))
print(adder2(1, 2))
print(adder2(1, 2, 3))
print(adder2(5.0, 10.0))
print(adder2('a', 'b'))
print(adder2([1], [2]))
