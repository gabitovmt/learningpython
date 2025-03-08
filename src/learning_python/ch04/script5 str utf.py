# Строки Unicode

print('sp\xc4m')
print(b'a\x01c')
print(u'sp\u00c4m')

print('spam'.encode('utf8'))    # 4 байта
print('spam'.encode('utf16'))   # 10 байт

print('sp\xc4\u00c4\U000000c4m')

print('\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1'))