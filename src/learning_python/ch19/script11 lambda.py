lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))    # aa
print(lower('aa', 'bb'))    # aa


import sys
showall = lambda x: list(map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])
# spam
# toast
# eggs
print(t)
# [5, 6, 5]

showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(['bright\n', 'side\n', 'of\n', 'life\n'])
# bright
# side
# of
# life
print(t)
# [7, 5, 3, 5]
