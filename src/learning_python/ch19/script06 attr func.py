# Интроспекция функций

def func(a):
    b = 'spam'
    return b * a
print(func(4))
# spamspamspamspam

print(func.__name__)
# func
print(dir(func))
# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__',
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__',
# '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__',
# '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__']

# Кодовый объект
print(func.__code__)
# <code object func at 0x000002AC43FA49D0, file "...\PycharmProjects\learningpython\src\learning_python\ch19\script06 attr func.py", line 3>
print(dir(func.__code__))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__replace__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '_co_code_adaptive', '_varname_from_oparg', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_exceptiontable',
# 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lines', 'co_linetable',
# 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_positions', 'co_posonlyargcount', 'co_qualname', 'co_stacksize',
# 'co_varnames', 'replace']
