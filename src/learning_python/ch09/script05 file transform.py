# Хранение объектов Python в файлах: преобразования

X, Y, Z = 43, 44, 45  # Собственные объекты Python. Для сохранения в файле обязаны быть строками
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))  # Преобразование чисел в строки
F.write(str(L) + '$' + str(D) + '\n')  # Преобразование и разделение посредством $
F.close()

chars = open('datafile.txt').read()
print(chars)
# Spam
# 43,44,45
# [1, 2, 3]${'a': 1, 'b': 2}

F = open('datafile.txt')
line = F.readline()
print(repr(line))
# 'Spam\n'
print(repr(line.rstrip()))  # Удаление символа конца строки
# 'Spam'

line = F.readline()  # Преобразование строки в целые числа
numbers = [int(x) for x in line.rstrip().split(',')]
print(repr(numbers))
# [43, 44, 45]

line = F.readline()
print(repr(line))
# "[1, 2, 3]${'a': 1, 'b': 2}\n"
objects = [eval(x) for x in line.split('$')]
print(repr(objects))
# [[1, 2, 3], {'a': 1, 'b': 2}]