# Файлы

myfile = open('myfile.txt', 'w')  # Открытие файла для текстового вывода: создание/очистка
print(myfile.write('hello text file\n'))  # Запись строки текста
# 16 - кол-во записанных символов - 3.x, 2.x - None
print(myfile.write('goodbye text file\n'))
# 18
myfile.close()  # Сброс выходных буферов на диск

myfile = open('myfile.txt')  # Открытие файла для текстового ввода
print(myfile.readline(), end='')
# hello text file
print(myfile.readline(), end='')
# goodbye text file
print(myfile.readline())
# - пустая строка: конец файла

print(open('myfile.txt').read())  # Чтение сразу всего файла в строковый объект

for line in open('myfile.txt'):  # Использование файловых итераторов
    print(line, end='')
