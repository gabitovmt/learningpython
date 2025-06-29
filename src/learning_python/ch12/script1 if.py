# Множественное ветвление
x = 'killer rabbit'
if x == 'roger':
    print('shave and a haircut')
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away! Run away!')
# Run away! Run away!

choice = 'ham'
print({'spam': 1.25,  # Аналог switch на основе словаря
       'ham': 1.99,
       'eggs': 0.99,
       'bacon': 1.10}[choice])
# 1.99

# Эквивалентный оператор if
if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice!')
# 1.99

branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}
print(branch.get('spam', 'Bad choice!'))
# 1.25
print(branch.get('meat', 'Bad choice!'))
# Bad choice!

choice = 'bacon'
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice!')
# 1.1

try:
    print(branch[choice])
except KeyError:
    print('Bad choice!')
# 1.1
