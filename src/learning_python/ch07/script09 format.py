# Вызовы методов форматирования строк

# По позициям
template = '{0}, {1} and {2}'
print(template.format('spam', 'ham', 'eggs'))
# spam, ham and eggs

# По ключевым словам
template = '{motto}, {pork} and {food}'
print(template.format(motto='spam', pork='ham', food='eggs'))

# По позициям и ключевым словам
template = '{motto}, {0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))

# По относительным позициям
template = '{}, {} and {}'
print(template.format('spam', 'ham', 'eggs'))

print('\n', ' Добавление ключей, атрибутов и смещений '.center(80, '-'))
import sys

print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
# My laptop runs win32
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))
# My laptop runs win32

somelist = list('SPAM')
print(somelist)
# ['S', 'P', 'A', 'M']
print('first={0[0]}, third={0[2]}'.format(somelist))
# first=S, third=A

# Отрицательные значения не допускаются в строке форматирования
print('first={0}, last={1}'.format(somelist[0], somelist[-1]))
# first=S, last=M

# Срезы не допускаются в строке форматирования
parts = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, middle={2}'.format(*parts))
# first=S, last=M, middle=['P', 'A']