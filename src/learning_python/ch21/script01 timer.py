# Модуль измерения времени: любительский

import time

def timer(func, *args):     # Упрощённая функция измерения времени
    start = time.time()
    for i in range(10_000):
        func(*args)
    return time.time() - start     # Суммарное истёкшее время в секундах


print(timer(pow, 2, 1000))      # Время, затраченное на вызов pow(2, 1000)
# 0.0025200843811035156
print(timer(str.upper, 'spam')) # Время, затраченное на вызов 'spam'.upper()
# 0.0002474784851074219
