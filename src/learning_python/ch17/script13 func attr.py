# Состояние с помощью атрибутов функций (3.X, 2.X)

def tester(start):
    def nested(label):
        print(label, nested.state)  # Функция nested находится в объемлющей области видимости
        nested.state += 1  # Изменяет атрибут, а не саму функцию nested
    nested.state = start   # Инициализация состояния после определения функции
    return nested


F = tester(0)
F('spam')  # F - это nested с присоединённым состоянием
# spam 0
F('ham')
# ham 1
print(F.state)  # Возможен также доступ к состоянию извне функции
# 2

G = tester(42)  # G имеет собственное состояние, состояние F не перезаписывается
G('eggs')
# eggs 42
F('ham')
# ham 2
print(F.state)  # Состояние доступно и поддерживается для каждого вызова
# 3
print(G.state)
# 43
print(F is G)  # Разные объекты функций
# False
