# Строки в действии
print('Базовые операции')

print(len('abc'))  # 3
print('abc' + 'def')  # abcdef
print('Ni!' * 4)  # Ni!Ni!Ni!Ni!
print('-' * 80)  # --------------------------------------------------------------------------------

my_job = 'hacker'
for c in my_job:
    print(c, end=' ')
# h a c k e r
print()
print('k' in my_job)  # True
print('z' in my_job)  # False
print('spam' in 'abcspamdef')  # True

print('\nИндексация и нарезание')
S = 'abcdefghijklmnop'
print(S[1:10:2])  # bdfhj
print(S[::2])  # acegikmo

S = 'hello'
print(S[::-1])  # olleh
S = 'abcedfg'
print(S[5:1:-1])  # Смысл границ изменяется: fdec

print()
print('spam'[1:3])  # Синтаксис нарезания
print('spam'[slice(1, 3)])  # Индексация посредством объектов срезов
print('spam'[::-1])
print('spam'[slice(None, None, -1)])

print('\nИнструменты преобразования строк')
print(int('42'), str(42))  # 42 42
# Преобразование в том виде, как она представлена в коде
print(repr(42))  # 42
print(repr('42'))  # '42'

print('\nПреобразования кодов символов')
print(ord('s'))  # 115
print(chr(115))  # s
