# Списковые включения
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print(L)
# [11, 12, 13, 14, 15]

L = [x + 10 for x in L]
print(L)
# [21, 22, 23, 24, 25]

# Использование списковых включений с файлами
f = open('text.txt', encoding='utf-8')
lines = f.readlines()
print(lines)
# ['Я помню чудное мгновенье:\n', 'Передо мной явилась ты,\n', 'Как мимолетное виденье,\n', 'Как гений чистой красоты.']

lines = [line.rstrip() for line in lines]
print(lines)
# ['Я помню чудное мгновенье:', 'Передо мной явилась ты,', 'Как мимолетное виденье,', 'Как гений чистой красоты.']

print('\nКонструкции фильтров: if')
lines = [line.rstrip() for line in open('text.txt', encoding='utf-8') if line[0] == 'К']
print(lines)
# ['Как мимолетное виденье,', 'Как гений чистой красоты.']

lines = [line.rstrip() for line in open('text.txt', encoding='utf-8') if line.rstrip()[-1:] == ',']
print(lines)
# ['Передо мной явилась ты,', 'Как мимолетное виденье,']

print('\nВложенные циклы: for')
r = [x + y for x in 'abc' for y in 'lmn']
print(r)
# ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
