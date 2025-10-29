#!python
# coding=utf-8
"""
reloadall.py: транзитивная перезагрузка вложенных модулей (Python 2.X + 3.X).
Вызывайте reload_all с одним и более объектами импортированных модулей.
"""

import sys
import types

if sys.version_info[0] == 3:
    if sys.version_info[1] == 0:
        from imp import reload
    else:
        from importlib import reload


def status(module):
    print('reloading ' + module.__name__)


def tryreload(module):
    try:
        reload(module)  # В 3.3 (только?) иногда терпело неудачу
    except:
        print('FAILED: %s' % module)


def transitive_reload(module, visited):
    if not module in visited:  # Отлавливать циклы, дубликаты
        status(module)  # Перезагрузить этот модуль
        tryreload(module)  # И посетить дочерние модули
        visited.add(module)
        for attrobj in module.__dict__.values():  # Для всех атрибутов
            if type(attrobj) == types.ModuleType:  # Рекурсивный вызов, если это модуль
                transitive_reload(attrobj, visited)


def reload_all(*args):
    visited = set()  # Главная точка входа
    for arg in args:  # Для всех переданных аргументов
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)


def tester(reloader, modname):  # Код самотестирования
    import importlib, sys  # Импортировать только при тестировании
    if len(sys.argv) > 1: modname = sys.argv[1]  # Командная строка (или переданный аргумент)
    module = importlib.import_module(modname)  # Импортировать по строке с именем
    reloader(module)  # Тестировать переданный аргумент reloader


if __name__ == '__main__':
    tester(reload_all, 'reloadall')  # Тест: перезагрузка самого себя?
