# Файлы с текстом Unicode

S = 'sp\xc4m'
print(S)
print(S[2])
file = open('unidata.txt', 'w', encoding='utf-8')
print(file.write(S))
file.close()

text = open('unidata.txt', encoding='utf-8').read()
print(text)
print(len(text))

print('\nЧтение закодированных байтов')
raw = open('unidata.txt', 'rb').read()
print(raw)
print(len(raw))

print('\nРучное кодирование и декодирование')
print(text.encode('utf-8'))
print(raw.decode('utf-8'))

print('\nРазные кодировки')
print(text.encode('latin-1'))
print(text.encode('utf-16'))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))