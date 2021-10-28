book = {}
i = 0
while i < 3:
    name = input('name ')
    age = int(input('age '))
    book[name] = age
    i += 1

name = input('Who do you want to figure out age? ')
print(f'{name} is {book[name]} years')
