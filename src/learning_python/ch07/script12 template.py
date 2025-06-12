# Template

import string
t = string.Template('$num = $title')

# 7 = Strings
print(t.substitute({'num': 7, 'title': 'Strings'}))
print(t.substitute(num=7, title='Strings'))