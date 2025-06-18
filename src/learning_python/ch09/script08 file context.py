# Модуль struct. Как и pickle, работает с двоичными данными.
# Может работать с двоичными данными на ЯП C, с сетевым подключением.

F = open('data_struct.bin', 'wb')
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
# Создание упакованных двоичных данных
# i - целое число, 4 байт
# 4s - строка bytes (3.2+), 4 - 4 байта
# h - целое число, 2 байта
# Обратный порядок байтов
print(data)
# b'\x00\x00\x00\x07spam\x00\x08'
F.write(data)
F.close()

# Чтение
F = open('data_struct.bin', 'rb')
data = F.read()
print(data)
# b'\x00\x00\x00\x07spam\x00\x08'
values = struct.unpack('>i4sh', data)
# Преобразовать в объекты Python
print(values)
# (7, b'spam', 8)