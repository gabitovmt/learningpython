# Состояние с помощью изменяемых объектов
# Не рекоммендуется

def tester(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1
    state = [start]
    return nested


F = tester(0)
F('spam')
# spam 0
F('ham')
# ham 1
