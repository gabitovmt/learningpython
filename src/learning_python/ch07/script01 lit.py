# Строковые литералы
print("Meaning " 'of' " Life")  # Неявная конкатенация

# Управляющие последовательности
print('a\nb\tc')

s = 'marat'
r = 'марат'
print(len(s), len(r))  # 5 5

print('Привет\b\b\bМир')  # ПриМир

print('\N{GREEK SMALL LETTER PI}')  # π

print('Непечатаемые символы выводятся в 16-ой форме')
print(repr('a\0b\0c'))  # 'a\x00b\x00c'
print(repr('\001\002\x03'))  # '\x01\x02\x03'

print('\\ в конце строки')
# print(r'C:\new\') - недопустимо нечётное количество \ в конце строки, даже для неформатированных строк
print(r'C:\new' + '\\')  # C:\new

# Многострочные блочные строки
print("""Always look
on the bright
side of life.""")
