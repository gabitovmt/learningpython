from M import func
from N import func  # Переписывает имя func, извлечённое из M
func()  # Вызывает только N.func!

print('-' * 80)
import M, N     # Получить модули целиком, не только их имена
M.func()        # Теперь мы можем обращаться к обоим именам
N.func()        # Указание имён модулей обеспечивает уникальность

print('-' * 80)
# Использование as
from M import func as mfunc # Переименование с помощью as
from N import func as nfunc
mfunc(); nfunc()        # Вызов одного или другого
