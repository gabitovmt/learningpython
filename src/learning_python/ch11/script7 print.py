# Перенаправление потока

import sys

sys.stdout.write('hello world\n')
# hello world

# Ручное перенаправление потока
sys.stdout = open('log.txt', 'a')  # Перенаправление вывода в файл
x, y, z = 1, 2, 3
print(x, y, z)  # Отправляется в log.txt

print('Bad!' * 8, file=sys.stderr)
# Bad!Bad!Bad!Bad!Bad!Bad!Bad!Bad!
