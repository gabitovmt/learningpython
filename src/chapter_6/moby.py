punct = ''.maketrans('.,;-', '    ')
words = set([])
with open('moby_01.txt') as infile:
    for line in infile:
        for word in line.lower().translate(punct).split():
            words.add(word)
words = list(words)
words.sort()

print('\n'.join(words), file=open('words', 'w'))
