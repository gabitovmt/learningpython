# nonlocal

def tester1(start):
    state = start  # Ссылка на нелокальные переменные работают нормально
    def nested(label):
        print(label, state)  # Запоминает state из объемлющей области видимости
    return nested

F = tester1(0)
F('spam')
# spam 0
F('ham')
# ham 0


# def tester2(start):
#     state = start
#     def nested(label):
#         print(label, state)
#         state += 1  # По умолчанию изменять нельзя (в Python 2.x вообще никогда)
#     return nested

# F = tester2(0)
# F('spam')
# UnboundLocalError


def tester3(start):
    state = start  # Каждый вызов получает собственное значение state
    def nested(label):
        nonlocal state  # Запоминает из объемлющей области видимости
        print(label, state)
        state += 1  # Нелокальную переменную разрешено изменять
    return nested

F = tester3(0)
F('spam')  # При каждом вызове state инкрементируется
# spam 0
F('ham')
# ham 1
F('eggs')
# eggs 2

G = tester3(42)  # Создание нового объекта функции tester, который начинает с 42
G('spam')
# spam 42
G('eggs')
# eggs 43
F('bacon')  # Функция F осталась там, где и была: 3
# bacon 3
