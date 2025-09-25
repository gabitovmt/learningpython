# Перестановки: все возможные комбинации
from src.learning_python.scramble import scramble
from src.learning_python.permute import permute1, permute2

print(list(scramble('abc')))    # Простое перемешивание: N
# ['abc', 'bca', 'cab']
print(permute1('abc'))          # Перестановок больше: N!
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(list(permute2('abc')))    # Генерация всех комбинаций
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

G = permute2('abc')
print(next(G))  # abc
print(next(G))  # acb

for x in permute2('abc'): print(x)
# abc
# acb
# bac
# bca
# cab
# cba

print('-' * 80)
print(permute1('spam') == list(permute2('spam')))
# True
print(len(list(permute2('spam'))), len(list(scramble('spam'))))
# 24 4
print(list(scramble('spam')))
# ['spam', 'pams', 'amsp', 'mspa']
print(list(permute2('spam')))
# ['spam', 'spma', 'sapm', 'samp', 'smpa', 'smap', 'psam', 'psma', 'pasm', 'pams', 'pmsa', 'pmas', 'aspm', 'asmp', 'apsm', 'apms', 'amsp', 'amps', 'mspa', 'msap', 'mpsa', 'mpas', 'masp', 'maps']
