# Строки
# Методы, специфичные для типа
S = 'Spam'
print(S.find('pa')) # 1
print(S.find('po')) # -1

print(S.replace('pa', 'XYZ'))
print(S)
print('-' * 10)

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))  # ['aaa', 'bbb', 'ccccc', 'dd']
print(S.upper())        # SPAM
print(S.isalpha())      # True
line = 'aaa,bbb,ccccc,dd\n'
print(line.rstrip())    # 'aaa,bbb,ccccc,dd'
print(line.rstrip().split(',')) # ['aaa', 'bbb', 'ccccc', 'dd']
print('-' * 10)

print('%s, eggs, and %s' % ('spam', 'SPAM!'))   # Выражение форматирования. Все версии
print('{0}, eggs, and {1}'.format('spam', 'SPAM'))  # Метод форматирования. 2.6+, 3.0+
print('{}, eggs, and {}'.format('spam', 'SPAM'))    # Метод форматирования. 2.7+, 3.1+
print('-' * 10)

print('{:,.2f}'.format(296999.2567))    # 296,999.26
print('%.2f | %+05d' % (3.14159, -42))  # 3.14 | -0042
print('-' * 10)

print(dir(S))