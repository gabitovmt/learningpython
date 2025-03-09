import random

print(random.random())  # Случайное число с плавающей точкой [0, 1)
print(random.randint(1, 10))  # Случайное целое число [1, 10]
print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))  # Случайный выбор

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)  # Тасование
print(suits)
