temperatures = []
with open('lab_05.txt', 'r') as f:
    for temperature in f.read().split():
        temperatures.append(float(temperature))

print('min: %.2f' % min(temperatures))
print('max: %.2f' % max(temperatures))
print('avg: %.2f' % (sum(temperatures) / len(temperatures)))
print('med: %.2f' % (sorted(temperatures)[len(temperatures) // 2]))
print('uniq: %d' % (len(set(temperatures))))
