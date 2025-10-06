import timeit

# Суммарное время
print(timeit.timeit(stmt='[x ** 2 for x in range(1000)]', number=1000))
# 0.08053869986906648

# API-интерфейс класса модуля
print(timeit.Timer(stmt='[x ** 2 for x in range(1000)]').timeit(1000))
# 0.18271589977666736
print(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=3))
# [0.09180549997836351, 0.07512299995869398, 0.09832469979301095]

def testcase():
    y = [x ** 2 for x in range(1000)]
# Вызываемые объекты или строки кода
print(min(timeit.repeat(stmt=testcase, number=1000, repeat=3)))
# 0.06272209994494915
