# Протокол итерации: итераторы файловых объектов
print(open('text.txt', encoding='utf-8').read())
print('-' * 80)

f = open('text.txt', encoding='utf-8')  # Чтение четырёхстрочного файла стиха в текущем каталоге
print(f.readline())  # При каждом вызове метод readline загружает одну строку
print(f.readline())
print(f.readline())
print(f.readline())  # Последние строки могут иметь или не иметь \n
print(f.readline())  # При достижении конца файла возвращается пустая строка
print('-' * 80)

f = open('text.txt', encoding='utf-8')  # При каждом вызове метод __next__ также загружает одну строку
print(f.__next__())  # Но при достижении конца файла генерирует исключение
print(f.__next__())
print(f.__next__())
print(f.__next__())
# print(f.__next__()) StopIteration
print('-' * 80)

for line in open('text.txt', encoding='utf-8'):  # Использование итератора файлового объекта для чтения по строкам
    print(line.upper(), end='')  # Вызывает __next__, перехватывает StopIteration
print('\n' + '-' * 80)

for line in open('text.txt', encoding='utf-8').readlines():  # Более ресурсоёмкий по памяти. Большие файлы не откроет
    print(line.upper(), end='')
print('\n' + '-' * 80)

f = open('text.txt', encoding='utf-8')
while True:  # Медленная версия
    line = f.readline()
    if not line: break
    print(line.upper(), end='')
print('\n' + '-' * 80)
