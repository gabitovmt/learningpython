with open('changer.py', 'w') as f:
    f.write('message = "First version"\n')
    f.write('def printer():\n')
    f.write('    print(message)\n')

import changer
changer.printer()
# First version

with open('changer.py', 'w') as f:
    f.write('message = "After editing"\n')
    f.write('def printer():\n')
    f.write('    print("reloaded:", message)\n')

import changer
changer.printer()
# First version

from importlib import reload
reload(changer)
changer.printer()
# reloaded: After editing
