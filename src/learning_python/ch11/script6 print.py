# Функция print()

x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep='...', end='!\n')

print(x, y, z, sep='...', file=open('data.txt', 'w'))
print(open('data.txt').read())
# spam...99...['eggs']