import sys

help(sys.getrefcount)
print('=' * 80)

help(sys)
# Информация о модуле отображается в структурированном виде.
print('=' * 80)

help('re')  # Можно указывать имя модуля

# help() - режим интерактивной справки

import docstrings
help(docstrings.square)
