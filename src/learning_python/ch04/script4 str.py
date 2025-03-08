# Строки
# Другие способы написания строк

S = 'A\nB\nC'
print(len(S))
print(ord('\n'))

S = 'A\0B\0C'
print(len(S))
print(S)

msg = """
aaa
bbb'''b""b'b
ccc
"""
print(msg)

print(r'C:\text\new')