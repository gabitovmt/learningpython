# Бесконечный цикл
# while True:
#     print('Type Ctrl-C to stop me!')

x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]
print()
# spam pam am m

a = 0; b = 10
while a < b: # Один способ написания циклов с подсчётом
    print(a, end=' ')
    a += 1
print()
# 0 1 2 3 4 5 6 7 8 9
