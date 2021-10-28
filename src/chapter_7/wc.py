import sys

lines_count = 0
words_count = 0
chars_count = 0

with open(sys.argv[1]) as infile:
    for line in infile:
        lines_count += 1
        chars_count += len(line)
        words_count += len(line.split())

print(f'File has {lines_count} lines, {words_count} words and {chars_count} chars')
