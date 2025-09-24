with open('myfile.txt', 'w') as f:
    f.write('aaa\nbbb\nccc\n')

print(open('myfile.txt').readlines())
# ['aaa\n', 'bbb\n', 'ccc\n']

print([line.rstrip() for line in open('myfile.txt').readlines()])
# ['aaa', 'bbb', 'ccc']
print([line.rstrip() for line in open('myfile.txt')])
# ['aaa', 'bbb', 'ccc']
print(list(map(lambda line: line.rstrip(), open('myfile.txt'))))
# ['aaa', 'bbb', 'ccc']

print('\nПример работы с БД')
listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]

print([age for (name, age, job) in listoftuple])
# [35, 40]
print(list(map(lambda row: row[1], listoftuple)))
# [35, 40]

# Только Python 2.X. tuple parameter unpacking is not supported in Python 3
# print(list(map(lambda (name, age, job): age, listoftuple)))
