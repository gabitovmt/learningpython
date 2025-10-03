from script04_timer2 import total, best_of, best_of_total

# По умолчанию 1K повторений
print(total(pow, 2, 1000)[0])
# 1K повторений
print(total(pow, 2, 1000, _reps=1000)[0])
# 1M повторений
print(total(pow, 2, 1000, _reps=1000_000)[0])

print('-' * 80)
# По умолчанию 5 повторений
print(best_of(pow, 2, 100_000)[0])
# Лучшее из 30
print(best_of(pow, 2, 100_000, _reps=30)[0])

print('-' * 80)
# Лучшее из 30, суммарное из 1K
print(best_of_total(str.upper, 'spam', _reps1=30, _reps=1000))

# Вложенные вызовы тоже работают
print(best_of(total, str.upper, 'spam', _reps=30))

print('-' * 80)
def spam(a, b, c, d): return a + b + c + d
print(total(spam, 1, 2, c=3, d=4, _reps=1000))
print(best_of(spam, 1, 2, c=3, d=4, _reps=1000))
print(best_of_total(spam, 1, 2, c=3, d=4, _reps1=1000, _reps=1000))
print(best_of_total(spam, *(1, 2), _reps1=1000, _reps=1000, **dict(c=3, d=4)))
