# Переопределение встроенных имён

def hider():
    open = 'spam' # Локальная переменная, скрывает здесь встроенное имя
    open('data.txt')
    # При вызове hider() будет TypeError. open больше не открывает файл

X = 88
def func():
    X = 99

func()
print(X)
# 88
