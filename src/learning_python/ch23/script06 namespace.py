import module2
# starting to load ...
# done loading.

print(module2.sys)
# <module 'sys' (built-in)>
print(module2.name)
# 42
print(module2.func)
# <function func at 0x000002BCC76B0B80>
print(module2.klass)
# <class 'module2.klass'>


print(list(module2.__dict__))
# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'sys', 'name', 'func', 'klass']
print(list(name for name in module2.__dict__ if not name.startswith('__')))
# ['sys', 'name', 'func', 'klass']
