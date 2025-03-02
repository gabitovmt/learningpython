"""Подсчёт количества строк, слов, символов"""
import argparse


def count(filename):
    """Подсчёт количества строк, слов, символов"""
    lines_count = 0
    words_count = 0
    chars_count = 0
    with open(filename) as file:
        for line in file:
            lines_count += 1
            words_count += len(line.split())
            chars_count += len(line)
    return {'lines_count': lines_count, 'words_count': words_count, 'chars_count': chars_count}


def _print(filename, counts, show_lines, show_words, show_chars):
    if show_lines == show_words == show_chars is False:
        show_lines = show_words = show_chars = True
    print(f'File {filename} has')
    if show_lines:
        print(f'{counts["lines_count"]} lines')
    if show_words:
        print(f'{counts["words_count"]} words')
    if show_chars:
        print(f'{counts["chars_count"]} chars')


def main():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('filename', help='read data from this file', metavar='FILE')
    parser.add_argument('-l', dest='lines', action='store_true', default=False, help='Count lines')
    parser.add_argument('-w', dest='words', action='store_true', default=False, help='Count words')
    parser.add_argument('-c', dest='chars', action='store_true', default=False, help='Count chars')
    args = parser.parse_args()

    _print(args.filename, count(args.filename), args.lines, args.words, args.chars)


if __name__ == '__main__':
    main()
