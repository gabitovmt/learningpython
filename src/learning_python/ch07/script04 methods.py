# Методы строковых и байтовых объектов

print('s.isalnum() - True, если все символы буквы/цифры')
print(''.isalnum())  # False
print('abc123 '.isalnum())  # False
print('abc123'.isalnum())  # True

print('\ns.isalpha() - True, если все символы буквы')
print('abc123'.isalpha())  # False
print('abc'.isalpha())  # True

print('\ns.isdecimal() - True, если все символы цифры. Unicode')
print('abc123'.isdecimal())  # False
print('123'.isdecimal())  # True
print('012\u06f0\u06f1\u06f2'.isdecimal())  # True
print('½'.isdecimal())  # False
print('²³'.isdecimal())  # False

print('\ns.isdigit() - True, если все символы цифры')
print('123'.isdigit())  # True
print('012\u06f0\u06f1\u06f2'.isdigit())  # True
print('½'.isdigit())  # False
print('²³'.isdigit())  # True

print('\ns.isidentifier() - True, если является действительный идентификатором в Python')
print('123'.isidentifier())  # False
print('abc123'.isidentifier())  # True
print('class'.isidentifier())  # True

print('\n.islower()')
print('123'.islower())  # False
print('абв'.islower())  # True
print('Абв'.islower())  # False

print('\ns.isnumeric() - True, если все символы цифры. Unicode')
print('123'.isnumeric())  # True
print('012\u06f0\u06f1\u06f2'.isnumeric())  # True
print('½'.isnumeric())  # True
print('²³'.isnumeric())  # True

print('\ns.isprintable() - True, если все символы - пробел \x20 или в Unicode определены как печатаемые символы')
print('a b'.isprintable())  # True
print('\x00'.isprintable())  # False

print('\ns.isspace() - True, если все символы пробельные')
print(' \t\v\n\r'.isspace())  # True
print('a'.isspace())  # False

print('\ns.istitle() - True, если непрерывная последовательность букв начинается с прописной буквы, \
а все остальные буквы нижнего регистра')
print('King Lear'.istitle())  # True
print('1900'.istitle())  # False
print('Troilus and Cressida'.istitle())  # False

print('\ns.isupper()')
print('123'.isupper())  # False
print('Абв'.isupper())  # False
print('АБВ'.isupper())  # True

print('\ns.isascii()')
print('Hello, world!'.isascii()) # True
print('Привет, мир!'.isascii()) # False
