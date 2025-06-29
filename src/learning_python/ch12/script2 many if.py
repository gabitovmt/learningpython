# Ограничители блоков
x = 'SPAM'  # Первая строка не должна иметь отступ
if 'rubbery' in 'shrubbery':
    print(x * 8)
    # SPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAM
    x += 'NI'  # Весь вложенный блок идёт с одинаковым отступом
    if x.endswith('NI'):
        x *= 2  # Другой вложенный блок
        print(x)
        # SPAMNISPAMNI
