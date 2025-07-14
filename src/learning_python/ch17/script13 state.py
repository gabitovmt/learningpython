# Состояние с помощью оператора nonlocal

def tester1(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester1(0)
F('spam')
# spam 0

# Переменная state видима только внутри замыкания
# F.state
# AttributeError


def tester2(start):
    global state  # Вынести в модуль, чтобы можно было изменять
    state = start  # global делает возможными изменения в области видимости модуля

    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester2(0)
F('spam')  # Каждый вызов инкрементирует разделяемое глобальное состояние
# spam 0
F('eggs')
# eggs 1

G = tester2(42)  # Сбрасывает единственную копию state в глобальной области видимости
G('toast')
# toast 42
G('bacon')
# bacon 43
F('ham')  # Но мой счётчик был перезаписан!
# ham 44


class tester3:  # Альтернатива на основе класса
    def __init__(self, start):  # При создании объектов состояние явно сохраняется в новом объекте
        self.state = start
    def nested(self, label):
        print(label, self.state)  # Явная ссылка на состояние
        self.state += 1  # Изменения также разрешены

F = tester3(0)  # Создание экземпляра, вызов __init__
F.nested('spam')  # F передаётся аргументу self
# spam 0
F.nested('ham')
# ham 1
G = tester3(42)  # Каждый экземпляр получает новую копию состояния
G.nested('toast')  # Изменение одного не влияет на остальные
# toast 42
G.nested('bacon')
# bacon 43
F.nested('eggs')  # Состояние F осталось прежним
# eggs 2
print(F.state)  # Доступ к состоянию возможен извне класса
# 3


class tester4:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):  # Перехватывает прямые обращения к экземпляру
        print(label, self.state)  # Таким образом, .nested() не требуется
        self.state += 1

H = tester4(99)
H('juice')  # Вызывает __call__
# juice 99
H('pancakes')
# pancakes 100


