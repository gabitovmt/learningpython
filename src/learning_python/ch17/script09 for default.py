# Переменные цикла и стандартные значения
def makeActions1():
    acts = []
    for i in range(5):  # Попытка запомнить каждое значение i
        acts.append(lambda x: i ** x)  # Но все функции запоминают последнее значение i
    return acts
acts = makeActions1()
print(acts[0])
# <function makeActions.<locals>.<lambda> at 0x0000025AAD75F9C0>

# Все возвращают 4 ** 2
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[4](2))


def makeActions2():
    acts = []
    for i in range(5):  # Использование стандартных значений
        acts.append(lambda x, i=i: i ** x)  # Запоминает текущее значение i
    return acts
acts = makeActions2()
print(acts[0](2))  # 0
print(acts[1](2))  # 1
print(acts[2](2))  # 4
print(acts[4](2))  # 16
