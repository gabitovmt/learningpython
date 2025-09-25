# Перестановки: все возможные комбинации
def permute1(seq):
    if not seq:         # Тасование любой последовательности: список
        return [seq]    # Пустая последовательность
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]      # Удаление текущего узла
            for x in permute1(rest):        # Перестановка остальных
                res.append(seq[i:i+1] + x)  # Добавление узла спереди
        return res

def permute2(seq):
    if not seq:         # Тасование любой последовательности: генератор
        yield seq       # Пустая последовательность
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]      # Удаление текущего узла
            for x in permute2(rest):        # Перестановка остальных
                yield seq[i:i+1] + x        # Добавление узла спереди
