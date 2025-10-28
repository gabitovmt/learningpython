import sys
print(sys.path)
# [
# 'D:\\Projects\\PycharmProjects\\learningpython\\src\\learning_python\\ch25',
# 'D:\\Projects\\PycharmProjects\\learningpython',
# 'C:\\Program Files\\JetBrains\\PyCharm 2025.1.1.1\\plugins\\python-ce\\helpers\\pycharm_display',
# 'D:\\Projects\\PycharmProjects\\learningpython\\.venv\\Scripts\\python313.zip',
# 'C:\\DevPrograms\\Python\\Python313\\DLLs',
# 'C:\\DevPrograms\\Python\\Python313\\Lib',
# 'C:\\DevPrograms\\Python\\Python313',
# 'D:\\Projects\\PycharmProjects\\learningpython\\.venv',
# 'D:\\Projects\\PycharmProjects\\learningpython\\.venv\\Lib\\site-packages',
# 'C:\\Program Files\\JetBrains\\PyCharm 2025.1.1.1\\plugins\\python-ce\\helpers\\pycharm_matplotlib_backend',
# 'C:\\Program Files\\JetBrains\\PyCharm 2025.1.1.1\\plugins\\python-ce\\helpers\\pycharm_plotly_backend'
# ]

sys.path = []
print(sys.path)
# []

import string
print(string)
# <module 'string' from 'C:\\DevPrograms\\Python\\Python313\\Lib\\string.py'>
# Когда через консоль выполнял, то ModuleNotFoundError: No module named 'string'
