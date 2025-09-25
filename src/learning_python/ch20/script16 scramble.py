from src.learning_python.scramble import scramble
from src.learning_python.inter import intersect, union


def tester(func, items, trace=True):
    for args in scramble(items):
        if trace: print(args)
        print(sorted(func(*args)))


tester(intersect, ('aab', 'abcde', 'ababab'))
print('-' * 80)
# ('aab', 'abcde', 'ababab')
# ['a', 'b']
# ('abcde', 'ababab', 'aab')
# ['a', 'b']
# ('ababab', 'aab', 'abcde')
# ['a', 'b']

tester(union, ('aab', 'abcde', 'ababab'))
print('-' * 80)
# ('aab', 'abcde', 'ababab')
# ['a', 'b', 'c', 'd', 'e']
# ('abcde', 'ababab', 'aab')
# ['a', 'b', 'c', 'd', 'e']
# ('ababab', 'aab', 'abcde')
# ['a', 'b', 'c', 'd', 'e']
