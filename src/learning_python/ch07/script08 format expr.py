# Выражения форматирования строк

exclamation = 'Ni'
print('The knights who say %s!' % exclamation)
# The knights who say Ni!

# Подстановки, специфичные для типов
print('%d %s %g you' % (1, 'spam', 4.0))
# 1 spam 4 you

# Все типы соответствуют цели %s
print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]))
# 42 -- 3.14159 -- [1, 2, 3]