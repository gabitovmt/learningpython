# Методы строковых и байтовых объектов

print('s.splitlines()')
print('ab c\n\nde fg\rkl\r\n'.splitlines())
print('ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))

print(''.split(), ''.splitlines())  # [] []
print('\n'.split(), '\n'.splitlines())  # [] ['']

print('One line\n'.splitlines())  # ['One line']
print('Two lines\n'.split('\n'))  # ['Two lines', '']

print('\ns.startswith()')
print('banana'.startswith('ba'))  # True
print('banana'.startswith('na'))  # False
print('banana'.startswith('na', 2))  # True

print('\ns.strip()')
print('banana'.strip('ab'))  # nan

print('\ns.swapcase()')
print('El Camino'.swapcase())  # eL cAMINO

print('\ns.title()')
print('Яблоко, апельсин, банан'.title())  # Яблоко, Апельсин, Банан
print('ORANGE'.title())  # Orange

print('\ns.upper()')
print('Яблоко'.upper())  # ЯБЛОКО

print('\ns.zfill()')
print('42'.zfill(5))  # 00042
print('+42'.zfill(5))  # +0042
print('-42'.zfill(5))  # -0042
print('123'.zfill(1))  # 123
