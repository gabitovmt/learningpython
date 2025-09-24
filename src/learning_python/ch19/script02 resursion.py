# Косвенная рекурсия

def mysum(L):
    if not L: return 0
    return nonempty(L)  # Вызов функции nonempty, которая вызывает mysum

def nonempty(L):
    return L[0] + mysum(L[1:])  # Косвенная рекурсия

print(mysum([1.1, 2.2, 3.3, 4.4]))
# 11.0
