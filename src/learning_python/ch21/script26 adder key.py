# Упражнения части IV. Ключевые аргументы

def adder(good=1, bad=2, ugly=3):
    return good + bad + ugly


print(adder())  # 6
print(adder(10))  # 15
print(adder(bad=10))  # 14
print(adder(bad=10, ugly=20))  # 31

print(adder(0))
print(adder(0, 0))
print(adder(0, 0, 0))
# print(adder(0, 0, 0, 0))  TypeError

print(adder(ugly=1, good=2))  # 5


def adder(**kargs):
    return sum(kargs.values())

print('-' * 80)
print(adder(a=5, b=4, c=3, d=2, e=1))
