print('banana'.translate({ord('a'): None, ord('n'): 'ze'}))

print('banana'.translate(''.maketrans('n', 'z', 'a')))