# Обобщённые функции для работы с множествами

# Пересечение
def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

# Объединение
def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res


s1, s2, s3 = 'SPAM', 'SCAM', 'SLAM'
print(intersect(s1, s2), union(s1, s2))
# ['S', 'A', 'M'] ['S', 'P', 'A', 'M', 'C']
print(intersect([1, 2, 3], (1, 4)))
# [1]
print(intersect(s1, s2, s3))
# ['S', 'A', 'M']
print(union(s1, s2, s3))
# ['S', 'P', 'A', 'M', 'C', 'L']


# Перемещает местами items для тестирования
def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))

print('-' * 80)
tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
# ('abcdefg', 'abdst', 'albmcnd', 'a')
# ['a']
# ('abdst', 'albmcnd', 'a', 'abcdefg')
# ['a']
# ('albmcnd', 'a', 'abcdefg', 'abdst')
# ['a']
# ('a', 'abcdefg', 'abdst', 'albmcnd')
# ['a']

print('-' * 80)
tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']

print('-' * 80)
tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)
# ['a', 'b']
# ['a', 'b']
# ['a', 'b']
# ['a', 'b']

print('-' * 80)
print('Дубликаты не повторяются')
print(intersect([1, 2, 1, 3], (1, 1, 4)))
# [1]
print(union([1, 2, 1, 3], (1, 1, 4)))
# [1, 2, 3, 4]
tester(intersect, ('ababa', 'abcdefga', 'aaaab'), False)
# ['a', 'b']
# ['a', 'b']
# ['a', 'b']
