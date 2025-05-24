# Двоичные файлы
import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)
file = open('data.bin', 'wb')
print(file.write(packed))
file.close()
print('-' * 10)

data = open('data.bin', 'rb').read()
print(data)
print(data[4:8])
print(list(data))
print(struct.unpack('>i4sh', data))