# Файлы

f = open('data.txt', 'w')
print(f.write('Hello\n'))
print(f.write('world\n'))
f.close()

f = open('data.txt')
text = f.read()
print(text)
print(text.split())

for line in open('data.txt'):
    print(line)