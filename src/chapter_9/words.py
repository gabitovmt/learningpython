import sys
import codecs


def readfile(filename):
    with codecs.open(filename, 'r', 'utf_8_sig') as f:
        return f.read()


def clean(text):
    table = ''.maketrans('.,-:;!?–…', '         ')
    return text.translate(table).lower()


def words(text):
    return text.split()


def dictionary(wordlist):
    d = {}
    for word in wordlist:
        d[word] = d.get(word, 0) + 1
    return sorted(list(d.items()), key=lambda x: x[1], reverse=True)


print(dictionary(words(clean(readfile(sys.argv[1]))))[:5])
