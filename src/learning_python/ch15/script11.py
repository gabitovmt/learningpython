# Упражнения части III

# 1.
S = 'Привет, Мир!'
sum = 0
for x in S:
    print(ord(x))
    sum += ord(x)
print('Сумма: {}'.format(sum))

A = list(map(ord, S))
print(A)

# 2.
# for i in range(50):
#     print('hello %d\n\a' % i)

# 3.
d = {ord(x): x for x in 'spam'}
print(d)

for k in sorted(d.keys()):
    print(k, d[k])
