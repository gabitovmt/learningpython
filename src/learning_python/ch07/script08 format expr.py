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

print('\n' + ' Ещё примеры '.center(80, '-'))

x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
print(res)
# integers: ...1234...1234  ...001234

x = 1.23456789
print(x)
print('%e | %f | %g' % (x, x, x))
# 1.234568e+00 | 1.234568 | 1.23457
print('%E' % x)
# 1.234568E+00
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
# 1.23   | 01.23 | +001.2
print('%s' % x, str(x))
# 1.23456789 1.23456789
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))
# 0.333333, 0.33, 0.3333

print('\n' + ' Выражения форматирования, основанные на словаре '.center(80, '-'))
print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})

reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40}
print(reply % values)

print('\n' + ' Использование vars() '.center(80, '-'))
food = 'spam'
qty = 10
print(vars())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002870C2D7EF0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Projects\\MyProjects\\learningpython\\src\\learning_python\\ch07\\script08 format expr.py', '__cached__': None, 'exclamation': 'Ni', 'x': 1.23456789, 'res': 'integers: ...1234...1234  ...001234', 'reply': '\nGreetings...\nHello %(name)s!\nYour age is %(age)s\n', 'values': {'name': 'Bob', 'age': 40}, 'food': 'spam', 'qty': 10}

print('%(qty)d more %(food)s' % vars())
# 10 more spam