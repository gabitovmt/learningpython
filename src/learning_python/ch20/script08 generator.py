# Расширенный протокол генераторных функций: send или next

def gen():
    for i in range(10):
        X = yield i
        print(X)

G = gen()
print(next(G))      # Сначала должен вызываться next(), чтобы запустить генератор
# 0
print(G.send(77))   # Продвигается вперёд и отправляет значение выражению yield
# 77
# 1
print(G.send(88))
# 88
# 2
print(next(G))      # next() и X.__next__() отправляют None
# None
# 3
