# Фабричные функции: замыкания

def maker(N):
    def action(X):  # Создание и возвращение функции action
        return X ** N  # action сохраняет N из объемлющей области видимости

    return action


f = maker(2)
print(f)
# <function maker.<locals>.action at 0x0000025736C89440>
print(f(3))
# 9
print(f(4))
# 16
g = maker(3)  # g запоминает 3, f запоминает 2
print(g(4))  # 4 ** 3
# 64
print(f(4))  # 4 ** 2
# 16

# Использование lambda
def another_maker(N):
    return lambda X: X ** N  # Функции lambda тоже сохраняют состояние


h = maker(3)
print(h(4))
# 64
