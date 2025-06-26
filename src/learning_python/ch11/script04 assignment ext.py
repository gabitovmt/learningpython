seq = [1, 2, 3, 4]
a, b, c, *d = seq
print(a, b, c, d)
# 1 2 3 [4]

a, b, c, d, *e = seq
print(a, b, c, d, e)
# 1 2 3 4 []

a, b, *e, c, d = seq
print(a, b, c, d, e)
# 1 2 3 4 []

# a, *b, c, *d = seq  SyntaxError. Нельзя больше одного имени со *
# a, b = seq  ValueError. Слишком много значений для распаковки
# *a = seq  SyntaxError. Имя со * должно быть в списке или в кортеже
*a, = seq
print(a)
# [1, 2, 3, 4]
