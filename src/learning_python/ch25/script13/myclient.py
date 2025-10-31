import mymod

print(mymod.countchars('mymod.py'))
print(mymod.countlines('mymod.py'))
print(mymod.test('mymod.py'))

from mymod import *

print(countchars('mymod.py'))
print(countlines('mymod.py'))
print(test('mymod.py'))
