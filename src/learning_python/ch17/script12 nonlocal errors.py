# nonlocal. Граничные случаи

# def tester(start):
#     def nested(label):
#         nonlocal state  # Нелокальные переменные уже должны существовать в объемлющем def!
#         state = 0
#         print(label, state)
#     return nested
# SyntaxError


def tester(start):
    def nested(label):
        global state  # Глобальные переменные не обязаны существовать до их объявления
        state = 0  # Создаёт имя в области видимости модуля
        print(label, state)
    return nested
F = tester(0)
F('ABC')
# ABC 0
print(state)
# 0


# spam = 99
# def tester1():
#     def nested():
#         nonlocal spam  # Должна быть в def, а не в модуле!
#         print('Current=', spam)
#         spam += 1
#     return nested
# SyntaxError
