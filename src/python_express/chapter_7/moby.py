with open('moby_01.txt') as infile:
    text = infile.read()

z = ''.maketrans('.,;-', '    ')
words = text.translate(z).lower().split()

dictionary = {}
for word in words:
    dictionary[word] = dictionary.get(word, 0) + 1

rare_words = []
for word in dictionary.keys():
    if dictionary[word] == 1:
        rare_words.append(word)
rare_words.sort()
rare_words = '\n'.join(rare_words)

print(rare_words, file = open('words.txt', 'w'))
