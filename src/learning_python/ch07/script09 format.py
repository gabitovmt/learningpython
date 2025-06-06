# Вызовы методов форматирования строк

# По позициям
template = '{0}, {1} and {2}'
print(template.format('spam', 'ham', 'eggs'))

# По ключевым словам
template = '{motto}, {pork} and {food}'
print(template.format(motto='spam', pork='ham', food='eggs'))

# По позициям и ключевым словам
template = '{motto}, {0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))

# По относительным позициям
template = '{}, {} and {}'
print(template.format('spam', 'ham', 'eggs'))