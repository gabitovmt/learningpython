x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
for item in x:
    print(item.strip('"'))

y = 'Mississippi'
pIndex = y.rfind('p')
y = y[:pIndex] + y[pIndex+1:]
print(y)
