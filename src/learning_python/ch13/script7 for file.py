# Чтение файла
file = open('test.txt', encoding='utf-8')
while True:
    char = file.read(1) # Посимвольное чтение
    if not char: break # Пустая строка означает конец файла
    print(char, end='')

for char in open('test.txt', encoding='utf-8').read(): # Здесь файл сразу весь загружается в память!
    print(char, end='')

file = open('test.txt', encoding='utf-8')
while True:
    line = file.readline() # Чтение строка за строкой
    if not line: break
    print(line, end='') # Строка уже содержит \n

file = open('test.txt', 'rb')
while True:
    chunk = file.read(10) # Чтение байтовых порций: до 10 байтов
    if not chunk: break
    print(chunk, end='')
print()

for line in open('test.txt', encoding='utf-8').readlines():
    print(line, end='')

for line in open('test.txt', encoding='utf-8'):
    print(line, end='')
