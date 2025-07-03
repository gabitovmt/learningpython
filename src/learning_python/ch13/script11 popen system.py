# Команды оболочки и другое
import os

os.system("chcp 1251")

F = os.popen('dir')
print(F.readline().rstrip())  # Чтение строки за строкой
#  Том в устройстве D имеет метку Основной

F = os.popen('dir')
print(F.read(50))  # Чтение блоками заданного размера
#  Том в устройстве D имеет метку Основной
#  Серийный

print(os.popen('dir').readlines()[0])  # Чтение всех строк: индексация
#  Том в устройстве D имеет метку Основной

print(os.popen('dir').read()[:50]) # Чтение всего сразу: срез
#  Том в устройстве D имеет метку Основной
#  Серийный

for line in os.popen('dir'): # Цикл с файловым итератором строк
    print(line.rstrip())
#  Всё содержимое консоли выводится

print('-' * 80)

print(os.system('systeminfo'))
print('-' * 80)
# В PyCharm вывелась информация о системе

for line in os.popen('systeminfo'):
    print(line.rstrip())
# Информация о системе
print('-' * 80)
