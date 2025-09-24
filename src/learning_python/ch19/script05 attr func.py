# Косвенные вызовы функций: "первоклассные" объекты

def echo(message):
    print(message)

echo('Direct call')
# Direct call

x = echo
x('Indirect call') # Вызов объекта через имя x путём добавления ()
# Indirect call

def indirect(func, arg):
    func(arg)   # Вызов переданного объекта путём добавления ()
indirect(echo, 'Argument call!')
# Argument call!

schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
for (func, arg) in schedule:
    func(arg) # Вызов функций, встроенных в контейнер
# Spam!
# Ham!

def make(label):    # Создание функции без её вызова
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Spam')    # label в объемлющей области видимости предохраняется
F('Ham!')           # Вызов функции, возвращённой make
# Spam:Ham!
F('Eggs!')
# Spam:Eggs!
